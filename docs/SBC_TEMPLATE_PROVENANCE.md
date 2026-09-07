# SBC template provenance

The PDF format in `quarto-sbc` is derived from the classic LaTeX template distributed for events of the Sociedade Brasileira de Computação (SBC).

## Project-supplied reference package

The implementation for PR #2 was checked against the archive supplied by the project owner:

- archive: `sbc-template-latex.zip`
- SHA-256: `4f9afbf2428d8403de56c3ecbae2bb4e17ec5efe35debbc07184f24ee0d8430b`

Reference files inside that archive:

| File | SHA-256 | Integration status |
|---|---|---|
| `sbc-template.sty` | `dbe513d56dde32bedc53dcf7b9efba052ff1b3b747037ed2f284f7095a91e895` | Integrated as the normative layout resource; malformed characters occurring only in comments were normalized when committed as UTF-8. |
| `sbc.bst` | `d884c6793e4ea54d13f5c751b3d6f4ea529a62d0906cd9774f2ec350b394691f` | Reference bibliography style. Its header states that copying is allowed subject to the conditions inherited from `apalike.bst`. Exact vendoring remains an explicit PR #2 completion item. |
| `sbc-template.tex` | `7b1c4682b13c523968cea1ea367eda4477952e49628b1527312e040a6f3b776b` | Used as the behavioral reference for title, authors, affiliations, Abstract, Resumo and page layout. |

## Encoding policy

The historical `sbc-template.tex` supplied with the project contains both

```tex
\usepackage[utf8]{inputenc}
```

and

```tex
\usepackage[latin1]{inputenc}
```

in the same document. `quarto-sbc` intentionally does **not** reproduce that conflict. The Quarto adapter uses UTF-8 consistently.

## Adaptation policy

The project keeps the following distinction explicit:

1. **Normative SBC behavior** — page geometry, typography, title block, sections, captions, Abstract/Resumo and related LaTeX behavior come from `sbc-template.sty`.
2. **Quarto/Pandoc adapter** — `_extensions/sbc/template.tex` maps document metadata and Pandoc output into the commands expected by the SBC style.
3. **Web representation** — HTML is a companion scholarly representation and is not claimed to reproduce the SBC PDF layout pixel-for-pixel.

Any future modifications to the imported SBC resource should be documented here and should not be described as official SBC changes.
