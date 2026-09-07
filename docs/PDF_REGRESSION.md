# SBC PDF regression policy

The validation strategy separates stable editorial requirements from rendering details that can vary across TeX, font, PDF-text extraction, and operating-system updates.

## Blocking checks

CI treats the following as stable properties of the repository's canonical manuscript fixture:

- the rendered PDF exists and is non-empty;
- the page size is A4 within a small numeric tolerance;
- the generated TeX contains the canonical title, both fixture authors, and their expected `\inst{...}` associations;
- the generated TeX preserves the expected template flow through `\begin{document}`, `\maketitle`, `abstract`, and `resumo`;
- the rendered PDF exposes `Abstract`, `Resumo`, `Introduction`, the fixture citation `Knuth 1984`, `Background and Related Work`, and `References` in the expected editorial order;
- the downstream portability smoke test from the distribution workflow continues to render the installed `sbc-pdf` format successfully.

The checks are implemented in `scripts/check_sbc_pdf.py` using three complementary signals:

1. `pdfinfo` for stable PDF geometry;
2. the generated `index.tex` for exact title, author, institute-number, and template-wiring assertions;
3. `pdftotext` for user-visible editorial sections, author-year citation rendering, and their order.

The PDF text check is token-based rather than literal-character-based. This deliberately ignores extraction-only whitespace and punctuation differences while preserving the semantic sequence that readers should observe.

## Why exact names are checked in generated TeX

PDF text extraction is not a canonical representation of typeset text. Font encodings, glyph composition, ligatures, and extraction heuristics can alter whitespace or token boundaries even when the rendered page is correct. Therefore title, author identity, and SBC institute associations are verified in the generated TeX, where their exact integration into the adapter is stable and inspectable.

Quarto normalizes rich author metadata and exposes the denormalized `by-author` view for journal templates. The SBC adapter uses that normalized view for author names while retaining its SBC-specific institute metadata mapping.

This avoids weakening the regression contract: the rendered PDF is still required to expose the principal editorial sections and a valid author-year citation in the correct order, while exact metadata is checked at the stage where exact string comparison is meaningful.

## Citation compatibility

The SBC style contains a historical `hyperref` hook for `\@lbibitem`. When `natbib` is used by the Quarto PDF format, that legacy hook can overwrite `natbib`'s author-year label parser. The adapter therefore saves the `natbib` + `hyperref` definition during the preamble and restores it immediately after `\begin{document}`, after end-of-preamble hooks have completed.

The canonical fixture intentionally contains a real bibliography entry and citation. CI requires `Knuth 1984` to occur after `Introduction` and before `Background and Related Work`, so a bibliography-only occurrence cannot satisfy the citation regression check.

## Review and diagnostic artifacts

CI rasterizes the first page of `_manuscript/index.pdf` and uploads it as `sbc-first-page-preview`. The preview is intended for human review of title block, authors, affiliations, abstracts, citation rendering, whitespace, and overall SBC-like presentation.

CI also uploads `sbc-regression-diagnostics`, containing the generated TeX, extracted PDF text, and `pdfinfo` output. These diagnostics are retained even when a blocking check fails so regressions can be investigated without relying on large workflow logs.

The preview is informational: it is not compared pixel-for-pixel in CI.

## Why there is no pixel-perfect baseline

A binary or pixel-level image comparison would make routine TeX Live, font-rendering, PDF engine, and runner updates capable of breaking CI despite no meaningful editorial regression. For this repository, structural/editorial checks are therefore blocking while visual inspection remains an explicit review aid.

A future baseline may be introduced only for carefully selected geometric measurements or regions whose stability has been demonstrated across supported rendering environments.
