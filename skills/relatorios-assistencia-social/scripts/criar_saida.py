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

MODELO_NOME = "RELATORIO ASSISTÊNCIA SOCIAL SECA E ESTIAGEM 2025.docx"
MODELO_SHA256 = "E2309DFE4169496CA3507200D3B8CD162A5B4FEE44CC6A3C90A7F58E4F7642B9"


def raiz_plugin() -> Path:
    return Path(__file__).resolve().parents[3]


def sha256(caminho: Path) -> str:
    resumo = hashlib.sha256()
    with caminho.open("rb") as arquivo:
        for bloco in iter(lambda: arquivo.read(1024 * 1024), b""):
            resumo.update(bloco)
    return resumo.hexdigest().upper()


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
    parser.add_argument("--data", help="Data documental no formato AAAA-MM-DD.")
    parser.add_argument("--base", type=Path, help="Raiz alternativa para testes.")
    return parser.parse_args()


def main() -> int:
    args = analisar_argumentos()
    raiz = raiz_plugin()
    modelo = raiz / "template" / MODELO_NOME
    if not modelo.is_file():
        print(f"Modelo não encontrado: {modelo}", file=sys.stderr)
        return 2

    hash_atual = sha256(modelo)
    if hash_atual != MODELO_SHA256:
        print(
            "O modelo foi alterado. Faça nova inspeção e atualize as regras antes de gerar saídas.",
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
