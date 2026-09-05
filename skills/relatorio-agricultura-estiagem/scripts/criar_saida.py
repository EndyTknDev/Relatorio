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

MODELO_NOME = "RELATORIO_AGRICULTURA_ESTIAGEM_-_2025.docx"
MODELO_SHA256 = "752D715DBA725A84F4A5FE898D43E4092AA704D600F871D940D6EF78F00C70F0"


def raiz_plugin() -> Path:
    return Path(__file__).resolve().parents[3]


def sha256(caminho: Path) -> str:
    resumo = hashlib.sha256()
    with caminho.open("rb") as arquivo:
        for bloco in iter(lambda: arquivo.read(1024 * 1024), b""):
            resumo.update(bloco)
    return resumo.hexdigest().upper()


def localizar_modelo(raiz: Path) -> tuple[Path | None, list[Path]]:
    """Localiza o DOCX pelo hash e informa arquivos que estavam bloqueados."""
    pasta = raiz / "template"
    bloqueados: list[Path] = []
    if not pasta.is_dir():
        return None, bloqueados

    preferido = pasta / MODELO_NOME
    candidatos = [preferido] if preferido.is_file() else []
    candidatos.extend(
        arquivo
        for arquivo in sorted(pasta.glob("*.docx"))
        if arquivo != preferido and not arquivo.name.startswith("~$")
    )

    for arquivo in candidatos:
        try:
            if sha256(arquivo) == MODELO_SHA256:
                return arquivo, bloqueados
        except PermissionError:
            bloqueados.append(arquivo)
    return None, bloqueados


def data_documental(valor: str | None) -> date:
    if not valor:
        return datetime.now(ZoneInfo("America/Manaus")).date()
    for formato in ("%Y-%m-%d", "%d/%m/%Y"):
        try:
            return datetime.strptime(valor, formato).date()
        except ValueError:
            pass
    raise ValueError("Use a data no formato AAAA-MM-DD ou DD/MM/AAAA.")


def nome_seguro(nome: str) -> str:
    nome = re.sub(r'[<>:"/\\|?*]', "-", nome).strip().rstrip(".")
    if not nome.lower().endswith(".docx"):
        nome += ".docx"
    return nome


def analisar_argumentos() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Prepara uma cópia do modelo em outputs/<Mês> <Ano>."
    )
    parser.add_argument("--nome", required=True, help="Nome do arquivo DOCX de saída.")
    parser.add_argument(
        "--data", required=True, help="Data documental em AAAA-MM-DD ou DD/MM/AAAA."
    )
    parser.add_argument("--base", type=Path, help="Pasta-base alternativa para a saída.")
    parser.add_argument(
        "--raiz-plugin", type=Path, help="Raiz alternativa do plugin para testes."
    )
    return parser.parse_args()


def main() -> int:
    args = analisar_argumentos()
    raiz = args.raiz_plugin.resolve() if args.raiz_plugin else raiz_plugin()
    modelo, bloqueados = localizar_modelo(raiz)
    if modelo is None:
        if bloqueados:
            print(
                "O modelo está aberto ou bloqueado. Feche o arquivo no Word e tente novamente.",
                file=sys.stderr,
            )
            return 2
        print(
            "Modelo não localizado pelo hash esperado. Confirme o arquivo em template/; "
            "se ele mudou, refaça a inspeção antes de gerar saídas.",
            file=sys.stderr,
        )
        return 3

    try:
        data_ref = data_documental(args.data)
    except ValueError as erro:
        print(str(erro), file=sys.stderr)
        return 5

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
