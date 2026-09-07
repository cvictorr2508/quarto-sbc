# SBC PDF regression policy

The validation strategy separates stable editorial requirements from rendering details that can vary across TeX, font, PDF-text extraction, and operating-system updates.

## Blocking checks

CI treats the following as stable properties of the repository's canonical manuscript fixture:

- the rendered PDF exists and is non-empty;
- the page size is A4 within a small numeric tolerance;
- the generated TeX contains the canonical title and both fixture authors;
- the generated TeX preserves the expected template flow through `\begin{document}`, `\maketitle`, `abstract`, and `resumo`;
- the rendered PDF exposes `Abstract`, `Resumo`, `Introduction`, and `References` in the expected editorial order.

The checks are implemented in `scripts/check_sbc_pdf.py` using three complementary signals:

1. `pdfinfo` for stable PDF geometry;
2. the generated `index.tex` for exact title, author, and template-wiring assertions;
3. `pdftotext` for user-visible editorial sections and their order.

The PDF text check is token-based rather than literal-character-based. This deliberately ignores extraction-only whitespace and punctuation differences while preserving the semantic section sequence that readers should observe.

## Why exact names are checked in generated TeX

PDF text extraction is not a canonical representation of typeset text. Font encodings, glyph composition, ligatures, and extraction heuristics can alter whitespace or token boundaries even when the rendered page is correct. Therefore title and author identity are verified in the generated TeX, where their exact integration into the SBC adapter is stable and inspectable.

This avoids weakening the regression contract: the rendered PDF is still required to expose the principal editorial sections in the correct order, while exact metadata is checked at the stage where exact string comparison is meaningful.

## Visual review artifact

CI rasterizes the first page of `_manuscript/index.pdf` and uploads the PNG as a workflow artifact. The preview is intended for human review of title block, affiliations, abstracts, whitespace, and overall SBC-like presentation.

The preview is informational: it is not compared pixel-for-pixel in CI.

## Why there is no pixel-perfect baseline

A binary or pixel-level image comparison would make routine TeX Live, font-rendering, PDF engine, and runner updates capable of breaking CI despite no meaningful editorial regression. For this repository, structural/editorial checks are therefore blocking while visual inspection remains an explicit review aid.

A future baseline may be introduced only for carefully selected geometric measurements or regions whose stability has been demonstrated across supported rendering environments.
