# AGENTS.md

## Purpose

This repository develops a reusable Quarto format and Manuscript starter for scientific articles that require an SBC-compatible LaTeX presentation.

## Engineering principles

- Preserve scientific, bibliographic, and upstream-template provenance.
- Do not fabricate references, metadata, experimental results, or claims about SBC venue requirements.
- Treat supplied SBC template resources as external normative inputs and document their source and any adaptations.
- Prefer minimal Quarto/Pandoc compatibility layers over rewriting the SBC style from scratch.
- Keep the Quarto-facing implementation and repository engineering documentation in UTF-8 English.
- Preserve `resumo`/`Resumo` only where required by the SBC manuscript interface or regression fixture.
- Keep example scientific content generic and free of invented findings.
- Keep computational results traceable to machine-readable research outputs.
- Avoid running expensive, licensed, GPU, solver, or HPC workloads in publication workflows; consume frozen or persisted outputs instead.
- Rendering changes must include reproducible validation and must not weaken the downstream installation contract.
- Do not introduce pixel-perfect PDF/image checks unless the selected measurement is demonstrably stable across supported rendering environments.

## Repository contract

The repository has two supported reuse paths:

1. existing Quarto projects install the SBC format with `quarto add cvictorr2508/quarto-sbc`;
2. new research projects use the GitHub Template Repository scaffold.

Do not advertise `quarto use template cvictorr2508/quarto-sbc` as a stable interface unless the repository packaging is explicitly redesigned and validated for Quarto's extension-template mechanism.

## Validation

Before merging a change, run or verify the equivalent CI checks:

```bash
quarto check
quarto render
```

For rendering-related changes, also verify that:

- `scripts/check_sbc_pdf.py` passes against the canonical manuscript artifacts;
- the first-page preview is visually coherent;
- regression diagnostic artifacts are produced;
- a clean downstream Quarto Manuscript project can install the extension and render `sbc-pdf` successfully;
- GitHub Pages publication remains compatible with frozen computational outputs.

## Documentation and comments

Repository-facing documentation, workflow descriptions, code comments, commit messages, and new engineering notes should be written in English.

Historical SBC terminology such as `Resumo`, LaTeX command names, bibliographic titles, proper nouns, and verbatim upstream identifiers may remain when they are part of the publication interface or provenance record.

Any future modification to an imported SBC resource must be documented in `docs/SBC_TEMPLATE_PROVENANCE.md` and must not be described as an official SBC change unless supported by an authoritative upstream source.
