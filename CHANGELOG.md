# Changelog

All notable changes to `quarto-sbc` are documented in this file.

## [0.2.0] - 2026-09-07

First public release of the reusable Quarto SBC manuscript infrastructure.

### Added

- reusable `sbc-pdf` and `sbc-html` Quarto formats;
- SBC-compatible title, author, institute, affiliation, Abstract, and Resumo handling;
- Quarto Manuscript starter with `execute.freeze: auto`;
- GitHub Template Repository workflow for bootstrapping new research repositories;
- downstream installation smoke test using `quarto add cvictorr2508/quarto-sbc`;
- GitHub Pages publication with artifact/OIDC deployment and least-privilege permissions;
- hybrid PDF regression checks using generated TeX, `pdfinfo`, and tokenized PDF text;
- first-page visual preview and regression diagnostic artifacts in CI;
- documented provenance for the project-supplied SBC LaTeX resources;
- MIT license for original project code and documentation, with explicit third-party exclusions.

### Fixed

- normalized Quarto author metadata so SBC author names and institute markers render correctly;
- restored natbib/hyperref bibliography behavior after the historical SBC style hook so author-year citations render correctly;
- normalized UTF-8 handling instead of reproducing the conflicting encodings in the historical example document;
- corrected downstream portability tests to validate behavior rather than Quarto internal installation paths.

### Distribution

Two downstream paths are supported:

- existing Quarto project: `quarto add cvictorr2508/quarto-sbc`;
- new research repository: GitHub **Use this template**.

Direct `quarto use template cvictorr2508/quarto-sbc` is not advertised as a stable interface for this repository layout.
