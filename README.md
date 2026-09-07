# quarto-sbc

Reusable Quarto infrastructure for preparing scientific manuscripts with the LaTeX style of the Sociedade Brasileira de Computação (SBC), with reproducible HTML/PDF output and GitHub Pages publication.

> Status: development (`0.3.0-dev`). The repository now combines a reusable SBC custom format with a Quarto Manuscript starter.

## What this repository provides

- `sbc-pdf`: submission-oriented PDF using the project-supplied `sbc-template.sty`;
- HTML manuscript output for scholarly web publication;
- a root Quarto Manuscript project that serves as an executable starter;
- `execute.freeze: auto` so expensive scientific computations can be executed locally/HPC and their saved outputs reused during publication;
- CI validation with Quarto + TinyTeX;
- GitHub Pages publication through the `gh-pages` branch.

## Repository layout

```text
_quarto.yml
index.qmd
references.bib
_extensions/
  sbc/
    _extension.yml
    sbc-template.sty
    template.tex
docs/
  SBC_TEMPLATE_PROVENANCE.md
.github/workflows/
  render.yml
  publish.yml
AGENTS.md
```

## Render the manuscript

With Quarto installed:

```bash
quarto preview
quarto render
```

A full `quarto render` should be run locally before publishing. When executable `.qmd` content is added, commit the resulting `_freeze/` updates so GitHub Actions can publish without reproducing expensive or licensed experiments.

## Reuse in another research repository

Install only the SBC format extension:

```bash
quarto add cvictorr2508/quarto-sbc
```

The repository root is also structured as a reusable Quarto Manuscript starter. The intended project-bootstrap command is:

```bash
quarto use template cvictorr2508/quarto-sbc
```

The starter provides `_quarto.yml`, `index.qmd`, bibliography scaffolding, the SBC extension, and publication workflows. Adapt the scientific content to the target repository while keeping numerical claims traceable to research artifacts.

## GitHub Pages

`.github/workflows/publish.yml` follows the Quarto Manuscript publishing model: pushes to `main` render and publish the manuscript to the `gh-pages` branch. The workflow deliberately does not install a scientific Python/R/HPC environment; computational results should normally be rendered locally and preserved with Quarto freeze.

For a downstream repository, GitHub Actions must be allowed to write repository contents so the workflow can update `gh-pages`, and GitHub Pages must use that branch as its publication source.

## SBC compatibility

The PDF adapter maps Quarto/Pandoc metadata to the classic SBC title, author, institute, affiliation, `Abstract`, and `Resumo` structures. UTF-8 is used consistently rather than reproducing the conflicting UTF-8/Latin-1 declarations found in the historical example `.tex`.

The supplied historical `sbc.bst` is tracked by SHA-256 in `docs/SBC_TEMPLATE_PROVENANCE.md`. Its header identifies it as an `apalike` copy for SBC whose documented distinction is citation-label punctuation. The executable adapter therefore uses `apalike` with natbib configured for SBC-compatible author-year punctuation. Literal vendoring can be added later when required by a venue, preserving the original copying notice.

## Design principles

The SBC template is the normative source for publication layout; Quarto is the authoring, reproducibility, and publication layer. Scientific repositories should generate both the web manuscript and submission-oriented PDF from one scholarly source rather than maintain parallel article versions.

The HTML representation is a scholarly companion and is not intended to reproduce the SBC page layout pixel-for-pixel.

## Roadmap

1. ✅ Validate the minimal Quarto format extension and CI.
2. ✅ Integrate `sbc-template.sty` with documented provenance and UTF-8 adaptation.
3. ✅ Add SBC-specific front matter and bibliography compatibility.
4. ✅ Add a Quarto Manuscript starter suitable for research repositories.
5. ✅ Add a reusable GitHub Pages publication workflow based on frozen computational outputs.
6. Add visual/regression checks against the supplied SBC reference PDF.
7. Validate installation/bootstrap behavior from a clean downstream repository.
8. Tag the first stable release.

## Provenance

Development is based on the SBC LaTeX publication template supplied to the project and on Quarto's documented custom-format and manuscript mechanisms. Upstream resources remain attributable to their original authors/source; provenance and compatibility decisions are recorded under `docs/`.
