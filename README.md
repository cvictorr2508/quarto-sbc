# quarto-sbc

Reusable Quarto format extension for preparing scientific manuscripts with the LaTeX style of the Sociedade Brasileira de Computação (SBC), with support for reproducible HTML/PDF publication workflows.

> Status: early development (`0.1.0-dev`). The current PDF template is a compatibility scaffold; integration of the supplied authoritative SBC `.sty`/`.bst` resources is intentionally tracked as a separate step so their provenance/licensing and any UTF-8 compatibility adaptations can be documented explicitly.

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
    template.tex
template.qmd
.github/workflows/render.yml
AGENTS.md
```

## Try the starter template

With Quarto installed:

```bash
quarto render template.qmd --to sbc-html
quarto render template.qmd --to sbc-pdf
```

To install the extension into an existing Quarto project from GitHub, the intended distribution path is:

```bash
quarto add cvictorr2508/quarto-sbc
```

To start from the repository's reusable example/template, the intended path is:

```bash
quarto use template cvictorr2508/quarto-sbc
```

These commands will become part of the supported public interface once the initial rendering PR is validated.

## Design principles

The project treats the SBC template as the normative source for publication layout while keeping Quarto as the authoring and reproducibility layer. Scientific repositories should therefore be able to generate both a human-readable web manuscript and a submission-oriented PDF without duplicating the article source.

The Quarto-facing implementation uses UTF-8 consistently. Historical encoding declarations from legacy SBC examples will not be copied blindly; any compatibility changes will be documented.

## Roadmap

1. Validate the minimal Quarto format extension and CI.
2. Integrate the supplied SBC `sbc-template.sty` and `sbc.bst` resources with documented provenance.
3. Add SBC-specific author/affiliation, `Abstract`, `Resumo`, bibliography, caption, and section handling.
4. Add visual/regression checks against the supplied SBC reference PDF.
5. Add a Quarto Manuscript starter suitable for research repositories.
6. Add a reusable GitHub Pages publication workflow for downstream repositories.
7. Tag the first stable release.

## Provenance

The initial development is based on the SBC LaTeX publication template supplied to the project and on Quarto's documented custom-format and manuscript extension mechanisms. Upstream template files remain attributable to their original authors/source.
