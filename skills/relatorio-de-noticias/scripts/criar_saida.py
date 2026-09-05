#!/usr/bin/env python3
"""Cria uma cópia protegida do relatório de notícias na pasta mensal de saídas."""

from __future__ import annotations

import argparse
import hashlib
import re
import shutil
import sys
from datetime import date
from pathlib import Path


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

MODELO_NOME = "RELATÓRIO DE NOTÍCIAS.docx"
MODELO_SHA256 = "6EFFB346244CD5F94F0D51F731DD0525681B5C0B472D3FB674D665AF6D2C4605"


def raiz_plugin() -> Path:
    return Path(__file__).resolve().parents[3]


def sha256(caminho: Path) -> str:
    resumo = hashlib.sha256()
    with caminho.open("rb") as arquivo:
        for bloco in iter(lambda: arquivo.read(1024 * 1024), b""):
            resumo.update(bloco)
    return resumo.hexdigest().upper()


def localizar_modelo(raiz: Path) -> Path | None:
    pasta = raiz / "template"
    if not pasta.is_dir():
        return None
    for arquivo in sorted(pasta.glob("*.docx")):
        if sha256(arquivo) == MODELO_SHA256:
            return arquivo
    return None


def nome_seguro(nome: str) -> str:
    nome = re.sub(r'[<>:"/\\|?*]', "-", nome).strip().rstrip(".")
    if not nome.lower().endswith(".docx"):
        nome += ".docx"
    return nome


def analisar_argumentos() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Copia o modelo para outputs/<Mês> <Ano> sem alterar o original."
    )
    parser.add_argument("--nome", required=True, help="Nome do arquivo DOCX de saída.")
    parser.add_argument(
        "--data",
        required=True,
        help="Data do relatório no formato AAAA-MM-DD.",
    )
    parser.add_argument("--base", type=Path, help="Raiz alternativa para testes.")
    return parser.parse_args()


def main() -> int:
    args = analisar_argumentos()
    try:
        data_relatorio = date.fromisoformat(args.data)
    except ValueError:
        print("Data inválida. Use o formato AAAA-MM-DD.", file=sys.stderr)
        return 2

    raiz = raiz_plugin()
    modelo = localizar_modelo(raiz)
    if modelo is None:
        print(
            "Modelo não localizado em template/ pelo hash esperado. "
            f"Confirme a presença de '{MODELO_NOME}'. Se o arquivo mudou, "
            "refaça a inspeção e atualize a referência e o script.",
            file=sys.stderr,
        )
        return 3

    base = args.base.resolve() if args.base else raiz / "outputs"
    pasta = base / f"{MESES[data_relatorio.month - 1]} {data_relatorio.year}"
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
