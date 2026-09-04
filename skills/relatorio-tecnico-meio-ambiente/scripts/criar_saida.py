#!/usr/bin/env python3
"""Cria uma cópia de trabalho do modelo na pasta mensal de saídas."""

from __future__ import annotations

import argparse
import hashlib
import re
import shutil
import sys
from datetime import date, datetime
from pathlib import Path
from zoneinfo import ZoneInfo


MESES = (
    "Janeiro",
    "Fevereiro",
    "Março",
    "Abril",
    "Maio",
    "Junho",
    "Julho",
    "Agosto",
    "Setembro",
    "Outubro",
    "Novembro",
    "Dezembro",
)

# O nome do arquivo do modelo contém a grafia "AMBIEMTE" e pode chegar ao disco
# em formas Unicode diferentes. Por isso o modelo é localizado pelo hash, e o
# nome abaixo serve apenas para mensagens de erro.
MODELO_NOME = "RELATÓRIO TÉCNICO MEIO AMBIEMTE 2025 ATUALIZADO.docx"
MODELO_SHA256 = "CC824F0B892219EA8BE95200C5E08D1C3383B56B0DAFC0CADF29691375A9E4D7"


def raiz_plugin() -> Path:
    return Path(__file__).resolve().parents[3]


def sha256(caminho: Path) -> str:
    resumo = hashlib.sha256()
    with caminho.open("rb") as arquivo:
        for bloco in iter(lambda: arquivo.read(1024 * 1024), b""):
            resumo.update(bloco)
    return resumo.hexdigest().upper()


def localizar_modelo(raiz: Path) -> Path | None:
    """Retorna o .docx de template/ cujo conteúdo bate com MODELO_SHA256."""
    pasta = raiz / "template"
    if not pasta.is_dir():
        return None
    for arquivo in sorted(pasta.glob("*.docx")):
        if sha256(arquivo) == MODELO_SHA256:
            return arquivo
    return None


def data_documental(valor: str | None) -> date:
    if valor:
        return date.fromisoformat(valor)
    return datetime.now(ZoneInfo("America/Manaus")).date()


def nome_seguro(nome: str) -> str:
    nome = re.sub(r'[<>:"/\\|?*]', "-", nome).strip().rstrip(".")
    if not nome.lower().endswith(".docx"):
        nome += ".docx"
    return nome


def analisar_argumentos() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Prepara uma cópia do modelo na pasta outputs/<Mês> <Ano>."
    )
    parser.add_argument("--nome", required=True, help="Nome do arquivo DOCX de saída.")
    parser.add_argument("--data", help="Data do documento no formato AAAA-MM-DD.")
    parser.add_argument("--base", type=Path, help="Raiz alternativa para testes.")
    return parser.parse_args()


def main() -> int:
    args = analisar_argumentos()
    raiz = raiz_plugin()

    modelo = localizar_modelo(raiz)
    if modelo is None:
        print(
            "Modelo não localizado em template/ pelo hash esperado. "
            f"Confirme a presença de '{MODELO_NOME}'. Se o arquivo mudou, "
            "refaça a inspeção e atualize a referência e o script antes de gerar saídas.",
            file=sys.stderr,
        )
        return 3

    data_ref = data_documental(args.data)
    base = args.base.resolve() if args.base else raiz / "outputs"
    pasta = base / f"{MESES[data_ref.month - 1]} {data_ref.year}"
    pasta.mkdir(parents=True, exist_ok=True)

    destino = pasta / nome_seguro(args.nome)
    if destino.exists():
        print(f"A saída já existe e não foi sobrescrita: {destino}", file=sys.stderr)
        return 4
    shutil.copy2(modelo, destino)
    print(destino)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
