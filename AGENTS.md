# AGENTS.md

## Purpose

This repository develops a reusable Quarto format extension for scientific articles following the Sociedade Brasileira de Computação (SBC) LaTeX style.

## Engineering principles

- Preserve scientific and bibliographic provenance.
- Do not fabricate references, metadata, or claims about SBC requirements.
- Treat upstream SBC template files as external normative resources; document their source and any modifications.
- Prefer minimal Quarto/Pandoc adaptations over rewriting the SBC style from scratch.
- Keep UTF-8 throughout the Quarto-facing implementation.
- Keep the example document generic and free of invented scientific results.
- Changes to rendering behavior should include or update a reproducible example and CI validation.

## Validation

Before merging changes, attempt:

```bash
quarto check
quarto render template.qmd --to sbc-html
quarto render template.qmd --to sbc-pdf
```

If official SBC resources are vendored later, verify that the generated PDF remains visually compatible with the supplied reference template and document all compatibility changes.
