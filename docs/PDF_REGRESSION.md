# SBC PDF regression policy

The PDF validation strategy separates stable editorial requirements from rendering details that can vary across TeX, font, and operating-system updates.

## Blocking checks

CI treats the following as stable properties of the repository's canonical manuscript fixture:

- the rendered PDF exists and is non-empty;
- the page size is A4 within a small numeric tolerance;
- the canonical title and author names are present;
- `Abstract`, `Resumo`, `Introduction`, and `References` are present;
- those editorial markers occur in the expected document order.

The checks are implemented in `scripts/check_sbc_pdf.py` using metadata from `pdfinfo` and layout-preserving text extracted by `pdftotext`.

## Visual review artifact

CI rasterizes the first page of `_manuscript/index.pdf` and uploads the PNG as a workflow artifact. The preview is intended for human review of title block, affiliations, abstracts, whitespace, and overall SBC-like presentation.

The preview is informational: it is not compared pixel-for-pixel in CI.

## Why there is no pixel-perfect baseline

A binary or pixel-level image comparison would make routine TeX Live, font-rendering, PDF engine, and runner updates capable of breaking CI despite no meaningful editorial regression. For this repository, structural checks are therefore blocking while visual inspection remains an explicit review aid.

A future baseline may be introduced only for carefully selected geometric measurements or regions whose stability has been demonstrated across supported rendering environments.
