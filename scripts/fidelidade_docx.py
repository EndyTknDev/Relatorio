"""Verificações conservadoras de OOXML; não substituem inspeção visual."""
from __future__ import annotations

import argparse
from collections import Counter
from copy import deepcopy
import json
from pathlib import Path
from xml.etree import ElementTree as ET
from zipfile import ZipFile

W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
SPACE = '{http://www.w3.org/XML/1998/namespace}space'


def substituir_em_trecho(paragrafo, antigo, novo):
    """Substituição única em um w:t existente; recusa fronteiras de formatação."""
    if not antigo:
        raise ValueError('Texto antigo vazio.')
    nodes = list(paragrafo.iter(W + 't'))
    total = ''.join(n.text or '' for n in nodes)
    if total.count(antigo) != 1:
        raise ValueError('A substituição deve identificar uma única ocorrência.')
    matches = [n for n in nodes if antigo in (n.text or '')]
    if len(matches) != 1:
        raise ValueError('Substituição atravessa trechos; mapeie a formatação explicitamente.')
    node = matches[0]
    node.text = node.text.replace(antigo, novo, 1)
    if node.text != node.text.strip():
        node.set(SPACE, 'preserve')


def assinatura(node):
    if node is None:
        return None
    return (node.tag, tuple(sorted(node.attrib.items())), node.text or '',
            tuple(assinatura(c) for c in node))


def sem_texto(root):
    root = deepcopy(root)
    for node in root.iter(W + 't'):
        node.text = ''
        node.attrib.pop(SPACE, None)
    return assinatura(root)


def perfis(paragrafo):
    # Textos vazios não contam. Estilos/tema herdados são protegidos pelo pacote.
    result = []
    for run in paragrafo.iter(W + 'r'):
        if ''.join(n.text or '' for n in run.iter(W + 't')).strip():
            profile = assinatura(run.find(W + 'rPr'))
            if not result or result[-1] != profile:
                result.append(profile)
    return result


def comparar(modelo, saida):
    errors, warnings = [], []
    with ZipFile(modelo) as a, ZipFile(saida) as b:
        if set(a.namelist()) != set(b.namelist()):
            errors.append('Partes do pacote adicionadas/removidas: revisar autorização e relações.')
        for name in sorted(set(a.namelist()) & set(b.namelist())):
            old, new = a.read(name), b.read(name)
            if old == new:
                continue
            if not name.endswith('.xml'):
                errors.append(f'{name}: mídia ou relações alteradas; verificar alteração autorizada.')
                continue
            ra, rb = ET.fromstring(old), ET.fromstring(new)
            if sem_texto(ra) != sem_texto(rb):
                errors.append(f'{name}: estrutura/propriedades/conteúdo não textual alterados.')
            pa, pb = list(ra.iter(W + 'p')), list(rb.iter(W + 'p'))
            if len(pa) != len(pb):
                errors.append(f'{name}: quantidade de parágrafos mudou.')
            for i, (x, y) in enumerate(zip(pa, pb)):
                tx = ''.join(n.text or '' for n in x.iter(W + 't'))
                ty = ''.join(n.text or '' for n in y.iter(W + 't'))
                if tx == ty:
                    continue
                if perfis(x) != perfis(y):
                    errors.append(f'{name} parágrafo {i}: mudou a sequência de formatos com texto preenchido.')
                if len(ty) > max(80, len(tx) * 1.5):
                    warnings.append(f'{name} parágrafo {i}: expansão de {len(tx)} para {len(ty)} caracteres; conferir espaço no render.')
    return {'erros': errors, 'avisos': warnings, 'validacao_visual': 'obrigatória e não executada por este verificador'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('modelo', type=Path)
    parser.add_argument('saida', type=Path)
    args = parser.parse_args()
    result = comparar(args.modelo, args.saida)
    print(json.dumps(result, ensure_ascii=True, indent=2))
    return 1 if result['erros'] else 0


if __name__ == '__main__':
    raise SystemExit(main())
