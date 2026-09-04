#!/usr/bin/env python3
"""Cria uma cópia protegida do parecer na pasta mensal de saídas."""

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

MODELO_NOME = "PARECER_TECNICO_DEFESA_CIVIL.docx"
MODELO_SHA256 = "C7E35046D4DF414E1CA78E1C0927C2C602BB59381D652990DF41F92315C9323F"


def raiz_plugin() -> Path:
    return Path(__file__).resolve().parents[3]


def sha256(caminho: Path) -> str:
    resumo = hashlib.sha256()
    with caminho.open("rb") as arquivo:
        for bloco in iter(lambda: arquivo.read(1024 * 1024), b""):
            resumo.update(bloco)
    return resumo.hexdigest().upper()


def nome_seguro(nome: str) -> str:
    nome = re.sub(r'[<>:"/\\|?*]', "-", nome).strip().rstrip(".")
    if not nome.lower().endswith(".docx"):
        nome += ".docx"
    return nome


def analisar_argumentos() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Copia o parecer para outputs/<Mês> <Ano> sem alterar o template."
    )
    parser.add_argument("--nome", required=True, help="Nome do arquivo DOCX de saída.")
    parser.add_argument(
        "--data",
        required=True,
        help="Data do documento no formato AAAA-MM-DD.",
    )
    parser.add_argument("--base", type=Path, help="Raiz alternativa para testes.")
    return parser.parse_args()


def main() -> int:
    args = analisar_argumentos()
    try:
        data_documento = date.fromisoformat(args.data)
    except ValueError:
        print("Data inválida. Use o formato AAAA-MM-DD.", file=sys.stderr)
        return 2

    raiz = raiz_plugin()
    modelo = raiz / "template" / MODELO_NOME
    if not modelo.is_file():
        print(f"Modelo não encontrado: {modelo}", file=sys.stderr)
        return 3

    if sha256(modelo) != MODELO_SHA256:
        print(
            "O modelo foi alterado. Faça nova inspeção antes de gerar saídas.",
            file=sys.stderr,
        )
        return 4

    base = args.base.resolve() if args.base else raiz / "outputs"
    pasta = base / f"{MESES[data_documento.month - 1]} {data_documento.year}"
    pasta.mkdir(parents=True, exist_ok=True)

    destino = pasta / nome_seguro(args.nome)
    if destino.exists():
        print(f"A saída já existe e não foi sobrescrita: {destino}", file=sys.stderr)
        return 5

    shutil.copy2(modelo, destino)
    print(destino)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
