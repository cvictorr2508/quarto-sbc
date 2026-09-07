# quarto-sbc

Reusable Quarto format extension for preparing scientific manuscripts with the LaTeX style of the Sociedade Brasileira de Computação (SBC), with support for reproducible HTML/PDF publication workflows.

> Status: early development (`0.2.0-dev`). The PDF adapter now uses the project-supplied `sbc-template.sty` as its normative layout resource and is continuously rendered in CI.

## Goals

- provide reusable `sbc-html` and `sbc-pdf` Quarto formats;
- support a single-source scholarly workflow in `.qmd`;
- preserve a submission-oriented LaTeX/PDF output;
- support web publication of the same manuscript;
- remain suitable for reproducible research repositories where expensive experiments are executed separately from document rendering.

## Repository layout

```text
_extensions/
  sbc/
    _extension.yml
    sbc-template.sty
    template.tex
docs/
  SBC_TEMPLATE_PROVENANCE.md
template.qmd
references.bib
.github/workflows/render.yml
AGENTS.md
```

## Try the starter document

With Quarto installed:

```bash
quarto render template.qmd --to sbc-html
quarto render template.qmd --to sbc-pdf
```

To install the extension into an existing Quarto project from GitHub:

```bash
quarto add cvictorr2508/quarto-sbc
```

The next development increment adds a full Quarto Manuscript starter so downstream research repositories can begin with `quarto use template cvictorr2508/quarto-sbc` and publish the manuscript through GitHub Pages.

## SBC compatibility

The PDF adapter maps Quarto/Pandoc metadata to the classic SBC title, author, institute, affiliation, `Abstract`, and `Resumo` structures. The adapter uses UTF-8 consistently rather than reproducing the conflicting UTF-8/Latin-1 declarations found in the historical example `.tex`.

The supplied historical `sbc.bst` is tracked by SHA-256 in `docs/SBC_TEMPLATE_PROVENANCE.md`. Its own header identifies it as an `apalike` copy for SBC whose documented distinction is citation-label punctuation. The executable adapter therefore uses `apalike` with natbib configured for SBC-compatible author-year punctuation. Literal vendoring of the historical `.bst` can be added later when required, provided its original copying notice is preserved.

## Design principles

The project treats the SBC template as the normative source for publication layout while keeping Quarto as the authoring and reproducibility layer. Scientific repositories should therefore be able to generate both a human-readable web manuscript and a submission-oriented PDF without duplicating the article source.

The HTML representation is a scholarly companion to the PDF; it is not intended to reproduce the SBC page layout pixel-for-pixel.

## Roadmap

1. ✅ Validate the minimal Quarto format extension and CI.
2. ✅ Integrate `sbc-template.sty` with documented provenance and UTF-8 adaptation.
3. ✅ Add SBC-specific author/affiliation, `Abstract`, `Resumo`, bibliography compatibility, caption, and section handling.
4. Add a Quarto Manuscript starter suitable for research repositories.
5. Add a reusable GitHub Pages publication workflow based on frozen computational outputs.
6. Add visual/regression checks against the supplied SBC reference PDF.
7. Tag the first stable release.

## Provenance

Development is based on the SBC LaTeX publication template supplied to the project and on Quarto's documented custom-format and manuscript mechanisms. Upstream template resources remain attributable to their original authors/source; provenance and compatibility decisions are recorded under `docs/`.
