#!/usr/bin/env python3
"""Validate stable editorial properties of the rendered SBC PDF fixture."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

A4_WIDTH_PT = 595.28
A4_HEIGHT_PT = 841.89
PAGE_TOLERANCE_PT = 1.0

EXPECTED_TEX_SEQUENCE = [
    r"\title{A Reproducible Scientific Article with Quarto and the SBC Style}",
    "First Author",
    r"\inst{1}",
    "Second Author",
    r"\inst{2}",
    r"\begin{document}",
    r"\maketitle",
    r"\begin{abstract}",
    r"\begin{resumo}",
]

EXPECTED_PDF_SEQUENCE = [
    "Abstract",
    "Resumo",
    "Introduction",
    "Knuth 1984",
    "Background and Related Work",
    "References",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pdfinfo", required=True, type=Path)
    parser.add_argument("--text", required=True, type=Path)
    parser.add_argument("--tex", required=True, type=Path)
    return parser.parse_args()


def check_page_size(info: str) -> None:
    match = re.search(r"Page size:\s+([0-9.]+) x ([0-9.]+) pts", info)
    if not match:
        raise SystemExit("Could not determine PDF page size")

    width, height = map(float, match.groups())
    if (
        abs(width - A4_WIDTH_PT) > PAGE_TOLERANCE_PT
        or abs(height - A4_HEIGHT_PT) > PAGE_TOLERANCE_PT
    ):
        raise SystemExit(
            f"Expected A4 PDF, got {width:.2f} x {height:.2f} pts"
        )


def normalize_whitespace(value: str) -> str:
    """Collapse formatting-only whitespace while retaining exact wording."""
    return " ".join(value.split())


def find_sequence(text: str, markers: list[str], *, label: str) -> None:
    normalized_text = normalize_whitespace(text)
    positions: list[tuple[str, int]] = []

    for marker in markers:
        normalized_marker = normalize_whitespace(marker)
        position = normalized_text.find(normalized_marker)
        if position < 0:
            raise SystemExit(f"Missing expected {label} marker: {marker}")
        positions.append((marker, position))

    for (previous, previous_pos), (current, current_pos) in zip(
        positions, positions[1:]
    ):
        if previous_pos >= current_pos:
            raise SystemExit(
                f"Unexpected {label} order: {previous!r} must precede {current!r}"
            )


def tokenize(value: str) -> list[str]:
    """Return Unicode word tokens, ignoring extraction-only spacing/punctuation."""
    return re.findall(r"[^\W_]+", value.casefold(), flags=re.UNICODE)


def find_token_sequence(tokens: list[str], marker_tokens: list[str], start: int) -> int:
    if not marker_tokens:
        return start

    limit = len(tokens) - len(marker_tokens) + 1
    for index in range(start, limit):
        if tokens[index : index + len(marker_tokens)] == marker_tokens:
            return index
    return -1


def check_pdf_editorial_sequence(text: str) -> None:
    tokens = tokenize(text)
    if not tokens:
        raise SystemExit("No extractable text found in rendered PDF")

    cursor = 0
    for marker in EXPECTED_PDF_SEQUENCE:
        marker_tokens = tokenize(marker)
        position = find_token_sequence(tokens, marker_tokens, cursor)
        if position < 0:
            raise SystemExit(f"Missing expected PDF editorial marker: {marker}")
        cursor = position + len(marker_tokens)


def main() -> None:
    args = parse_args()
    info = args.pdfinfo.read_text(encoding="utf-8", errors="replace")
    text = args.text.read_text(encoding="utf-8", errors="replace")
    tex = args.tex.read_text(encoding="utf-8", errors="replace")

    check_page_size(info)
    find_sequence(tex, EXPECTED_TEX_SEQUENCE, label="generated TeX")
    check_pdf_editorial_sequence(text)
    print("SBC PDF editorial regression checks passed")


if __name__ == "__main__":
    main()
