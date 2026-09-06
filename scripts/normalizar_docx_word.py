#!/usr/bin/env python3
"""Normaliza um DOCX com LibreOffice para garantir abertura no Microsoft Word."""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import tempfile
import zipfile
from pathlib import Path

from docx import Document


def localizar_soffice() -> str:
    candidates = [
        shutil.which("soffice.com"),
        shutil.which("soffice"),
        r"C:\Program Files\LibreOffice\program\soffice.com",
    ]
    for candidate in candidates:
        if candidate and Path(candidate).is_file():
            return candidate
    raise FileNotFoundError(
        "LibreOffice não foi localizado. Instale-o ou disponibilize soffice no PATH."
    )


def validar_docx(path: Path) -> None:
    with zipfile.ZipFile(path) as pacote:
        if pacote.testzip() is not None:
            raise RuntimeError("O pacote DOCX normalizado contém uma entrada ZIP inválida.")
        if "[Content_Types].xml" not in pacote.namelist():
            raise RuntimeError("O pacote DOCX normalizado não contém [Content_Types].xml.")
    Document(path)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("entrada", type=Path, help="DOCX a normalizar.")
    output = parser.add_mutually_exclusive_group(required=True)
    output.add_argument("--saida", type=Path, help="Destino do DOCX normalizado.")
    output.add_argument("--in-place", action="store_true", help="Substitui a entrada após validação.")
    args = parser.parse_args()

    entrada = args.entrada.resolve()
    if not entrada.is_file() or entrada.suffix.lower() != ".docx":
        raise FileNotFoundError(f"DOCX de entrada não encontrado: {entrada}")
    destino = entrada if args.in_place else args.saida.resolve()
    if not args.in_place and destino == entrada:
        raise ValueError("Use --in-place para substituir o arquivo de entrada.")

    soffice = localizar_soffice()
    with tempfile.TemporaryDirectory(prefix="docx_word_", dir=entrada.parent) as temp:
        temp_dir = Path(temp)
        profile = temp_dir / "perfil-lo"
        command = [
            soffice,
            f"-env:UserInstallation={profile.as_uri()}",
            "--headless",
            "--nologo",
            "--nodefault",
            "--nolockcheck",
            "--convert-to",
            "docx",
            "--outdir",
            str(temp_dir),
            str(entrada),
        ]
        subprocess.run(command, check=True, capture_output=True, text=True)
        convertido = temp_dir / entrada.name
        if not convertido.is_file():
            raise RuntimeError("LibreOffice não produziu o DOCX normalizado.")
        validar_docx(convertido)
        if args.in_place:
            staging = entrada.with_suffix(".word-normalized.docx")
            shutil.copy2(convertido, staging)
            os.replace(staging, entrada)
        else:
            destino.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(convertido, destino)
        validar_docx(destino)
    print(destino)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
