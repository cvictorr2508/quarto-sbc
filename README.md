# quarto-sbc

Reusable Quarto infrastructure for preparing scientific manuscripts with the LaTeX style of the Sociedade Brasileira de Computação (SBC), with reproducible HTML/PDF output and GitHub Pages publication.

> **Status:** pre-release (`0.3.1-dev`). The core format, Quarto Manuscript starter, GitHub Pages workflow, downstream portability test, and PDF regression gate are implemented and validated. The remaining release step is to create the first stable tag after final repository sanitization.

## Overview

`quarto-sbc` provides a single-source workflow for researchers who want to author a scientific manuscript in Quarto while producing both a submission-oriented SBC PDF and a scholarly HTML version.

The repository includes:

- `sbc-pdf`, a custom Quarto PDF format based on the project-supplied `sbc-template.sty`;
- an HTML companion manuscript for web publication;
- a reusable Quarto Manuscript starter at the repository root;
- `execute.freeze: auto`, allowing computational results produced locally or on HPC to be reused during publication;
- continuous integration with Quarto, TinyTeX, structural PDF regression checks, and downstream installation validation;
- GitHub Pages publication through the official Pages artifact/OIDC deployment model;
- provenance documentation for the historical SBC LaTeX resources and all compatibility decisions.

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
scripts/
  check_sbc_pdf.py
docs/
  PDF_REGRESSION.md
  SBC_TEMPLATE_PROVENANCE.md
.github/workflows/
  render.yml
  publish.yml
AGENTS.md
```

Generated PDFs, TeX intermediates, Quarto build directories, and GitHub Actions artifacts are intentionally excluded from version control.

## Requirements

For local rendering, install a current release of [Quarto](https://quarto.org/). PDF rendering also requires a LaTeX distribution; TinyTeX is a convenient option and is installed automatically in GitHub Actions.

Check the local environment with:

```bash
quarto check
```

## Render the manuscript

From the repository root:

```bash
quarto preview
quarto render
```

The canonical manuscript output is written under `_manuscript/` and is not committed to the repository.

A full `quarto render` should be run locally before publication. When executable `.qmd` content is introduced, commit the relevant `_freeze/` updates so publication workflows can reuse expensive, licensed, or HPC-generated computations without rerunning them on GitHub-hosted runners.

## Use the SBC format in an existing research repository

From an existing Quarto project, install the public extension entry point:

```bash
quarto add cvictorr2508/quarto-sbc
```

Then select the format in document metadata:

```yaml
format:
  sbc-pdf: default
```

The implementation lives under `_extensions/sbc/`, but that internal repository path is not part of the downstream installation contract. CI validates portability by creating a clean Quarto Manuscript project, installing `cvictorr2508/quarto-sbc`, and rendering an SBC PDF from that independent project.

## Start a new research repository

This repository is configured as a **GitHub Template Repository**. For a new scientific project, use **Use this template** on GitHub to create a repository containing the complete scaffold, including `_quarto.yml`, `index.qmd`, `references.bib`, the SBC extension, and validation/publication workflows.

After creating a downstream repository:

1. replace the example manuscript metadata and scientific content;
2. keep references and empirical claims traceable to verifiable sources or machine-readable research outputs;
3. run `quarto render` locally;
4. if GitHub Pages is desired, open **Settings → Pages** and set **Source** to **GitHub Actions**.

A direct `quarto use template cvictorr2508/quarto-sbc` bootstrap is intentionally **not advertised as a stable interface**. The repository root is an executable Quarto Manuscript, whereas Quarto extension-template packaging follows a different convention. GitHub's Template Repository mechanism preserves the complete research scaffold without relying on that transformation.

## Manuscript metadata

The PDF adapter supports the SBC title block through Quarto metadata. A minimal example is:

```yaml
title: "Article title"
author:
  - name: First Author
    institute: 1
  - name: Second Author
    institute: 2
sbc-affiliations:
  - text: "Department or Institute -- University A -- City -- Country"
    email: "first.author@example.org"
  - text: "Department or Institute -- University B -- City -- Country"
    email: "second.author@example.org"
abstract: |
  English abstract.
resumo: |
  Portuguese abstract required when applicable to the target SBC venue.
bibliography: references.bib
```

The key name `resumo` and the rendered label `Resumo` are intentionally retained because they are part of the SBC publication structure; repository engineering documentation and code comments are maintained in English.

## Bibliography behavior

The historical `sbc.bst` supplied to the project identifies itself as a copy of `apalike` for SBC whose documented difference is the removal of the comma before the year in citation labels. The executable adapter therefore uses `apalike` together with natbib punctuation configured to reproduce that SBC author-year behavior.

The historical `.bst` is tracked by SHA-256 in `docs/SBC_TEMPLATE_PROVENANCE.md` rather than partially copied or silently modified. The canonical CI fixture checks that the author-year citation renders correctly.

## PDF regression policy

CI intentionally combines several complementary signals instead of relying on a pixel-perfect baseline:

- `pdfinfo` validates A4 page geometry;
- generated `index.tex` validates the canonical title, authors, institute markers, and SBC template wiring;
- tokenized PDF text validates the visible editorial sequence, including Abstract, Resumo, section headings, the bibliography fixture citation, and References;
- a 144 DPI first-page PNG is uploaded for human visual inspection;
- generated TeX, extracted PDF text, and PDF metadata are uploaded as diagnostic artifacts.

This design detects meaningful editorial regressions while avoiding false failures caused only by TeX Live, font-rendering, PDF-engine, or operating-system differences. See `docs/PDF_REGRESSION.md` for the complete policy.

## GitHub Pages

`.github/workflows/publish.yml` renders the Quarto Manuscript, uploads `_manuscript/` as a GitHub Pages artifact, and deploys it with `actions/deploy-pages`.

The workflow uses narrowly scoped permissions:

- `contents: read`;
- `pages: write`;
- `id-token: write`.

It deliberately does not install a project-specific Python, R, solver, GPU, or HPC environment. Computational results should normally be produced in the scientific repository's appropriate execution environment and consumed through Quarto freeze or committed machine-readable outputs.

## SBC compatibility and provenance

The SBC LaTeX template remains the normative source for submission layout. Quarto acts as the authoring, reproducibility, metadata-adaptation, and publication layer.

The adapter preserves the classic SBC page geometry, title block, author/institute associations, affiliations, Abstract/Resumo structures, and bibliography behavior while using UTF-8 consistently. It does not reproduce the conflicting UTF-8/Latin-1 declarations found in the historical example document.

The HTML manuscript is a scholarly companion representation and is not intended to reproduce the SBC PDF layout pixel-for-pixel.

All imported-resource provenance and compatibility decisions are documented in `docs/SBC_TEMPLATE_PROVENANCE.md`.

## Development and validation

Before merging a rendering change, the repository CI verifies:

```bash
quarto check
quarto render
```

It then runs the SBC PDF regression checker, publishes visual/diagnostic artifacts, and validates installation from a clean downstream Quarto Manuscript project.

Local contributors can also run the checker when the required artifacts have been prepared:

```bash
python3 scripts/check_sbc_pdf.py \
  --pdfinfo artifacts/index-pdfinfo.txt \
  --text artifacts/index.txt \
  --tex artifacts/index.tex
```

See `AGENTS.md` for repository engineering principles.

## Release readiness

The repository has completed the initial implementation milestones:

- reusable Quarto SBC format;
- SBC LaTeX style integration with documented provenance;
- metadata and bibliography compatibility;
- Quarto Manuscript starter;
- GitHub Pages artifact deployment;
- clean downstream extension installation/render validation;
- structural/editorial PDF regression checks;
- first-page visual review and regression diagnostics.

After the final sanitization PR is merged and the post-merge CI/Pages workflows remain green, the repository is ready for its first stable release tag.

## Scope and responsibility

This project is a research-oriented Quarto integration around the supplied SBC LaTeX resources. It should not be interpreted as an official publication-rules authority for every SBC venue. Researchers should always verify the current author instructions of the specific conference, journal, workshop, or event before submission.

Upstream SBC resources remain attributable to their original authors and source. Future changes to imported resources or venue-specific behavior should preserve provenance and be documented explicitly.
