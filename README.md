# quarto-sbc

Reusable Quarto infrastructure for preparing scientific manuscripts with the LaTeX style of the Sociedade Brasileira de Computação (SBC), with reproducible HTML/PDF output and GitHub Pages publication.

> Status: development (`0.3.1-dev`). The repository combines a reusable SBC custom format with a Quarto Manuscript starter and artifact-based GitHub Pages deployment.

## What this repository provides

- `sbc-pdf`: submission-oriented PDF using the project-supplied `sbc-template.sty`;
- HTML manuscript output for scholarly web publication;
- a root Quarto Manuscript project that serves as an executable starter;
- `execute.freeze: auto` so expensive scientific computations can be executed locally/HPC and their saved outputs reused during publication;
- CI validation with Quarto + TinyTeX;
- GitHub Pages publication using the official Pages artifact/OIDC deployment model rather than writing to a `gh-pages` branch.

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

There are two supported downstream paths, depending on whether a research repository already exists.

### Existing repository: install only the SBC format

From the target Quarto project, install the extension explicitly from its `sbc` subdirectory:

```bash
quarto add cvictorr2508/quarto-sbc/sbc
```

This installs `_extensions/sbc/` while leaving the target repository's scientific structure unchanged.

### New scientific repository: use this GitHub template

This repository is configured as a **GitHub Template Repository**. For a new research project, use **Use this template** on GitHub to create the new repository with the complete scaffold, including `_quarto.yml`, `index.qmd`, `references.bib`, `_extensions/sbc/`, and the validation/publication workflows.

After creating a downstream repository from the template, adapt the manuscript metadata and scientific content, then enable **Settings → Pages → Source: GitHub Actions** if GitHub Pages publication is desired.

A direct `quarto use template cvictorr2508/quarto-sbc` bootstrap is intentionally **not advertised as stable**. The repository root is an executable Quarto Manuscript (`index.qmd`), while Quarto's extension-template mechanism has different packaging conventions. The GitHub template-repository path preserves the complete Manuscript scaffold without relying on that transformation.

## GitHub Pages

`.github/workflows/publish.yml` renders the Quarto Manuscript, uploads `_manuscript/` as a GitHub Pages artifact, and deploys it with `actions/deploy-pages`. It uses narrowly scoped permissions:

- `contents: read`;
- `pages: write`;
- `id-token: write`.

The workflow deliberately does not install a scientific Python/R/HPC environment. Computational results should normally be generated locally or on HPC and preserved with Quarto freeze.

### One-time repository configuration

For this repository and for each downstream repository using the starter, open **Settings → Pages** and set **Source** to **GitHub Actions**. No personal access token and no repository-wide `contents: write` permission are required by the publication workflow.

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
5. ✅ Add a reusable GitHub Pages artifact-deployment workflow based on frozen computational outputs.
6. 🔄 Add structural/visual regression checks against the SBC reference output.
7. 🔄 Validate downstream extension installation and template-repository bootstrap behavior from a clean repository.
8. Tag the first stable release.

## Provenance

Development is based on the SBC LaTeX publication template supplied to the project and on Quarto's documented custom-format and manuscript mechanisms. Upstream resources remain attributable to their original authors/source; provenance and compatibility decisions are recorded under `docs/`.
