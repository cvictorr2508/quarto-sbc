#!/usr/bin/env python3
"""Validate stable editorial properties of the rendered SBC PDF fixture."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

A4_WIDTH_PT = 595.28
A4_HEIGHT_PT = 841.89
PAGE_TOLERANCE_PT = 1.0

EXPECTED_SEQUENCE = [
    "A Reproducible Scientific Article with Quarto and the SBC Style",
    "First Author",
    "Second Author",
    "Abstract",
    "Resumo",
    "Introduction",
    "References",
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--pdfinfo", required=True, type=Path)
    parser.add_argument("--text", required=True, type=Path)
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
    """Collapse extraction-only whitespace without changing visible wording."""
    return " ".join(value.split())


def check_editorial_sequence(text: str) -> None:
    normalized_text = normalize_whitespace(text)
    positions: list[tuple[str, int]] = []

    for marker in EXPECTED_SEQUENCE:
        normalized_marker = normalize_whitespace(marker)
        position = normalized_text.find(normalized_marker)
        if position < 0:
            raise SystemExit(f"Missing expected editorial marker: {marker}")
        positions.append((marker, position))

    for (previous, previous_pos), (current, current_pos) in zip(
        positions, positions[1:]
    ):
        if previous_pos >= current_pos:
            raise SystemExit(
                f"Unexpected editorial order: {previous!r} must precede {current!r}"
            )


def main() -> None:
    args = parse_args()
    info = args.pdfinfo.read_text(encoding="utf-8", errors="replace")
    text = args.text.read_text(encoding="utf-8", errors="replace")

    check_page_size(info)
    check_editorial_sequence(text)
    print("SBC PDF editorial regression checks passed")


if __name__ == "__main__":
    main()
