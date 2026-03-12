# gaia-skills

A template repository for hosting skill markdown files that externalize cultural practices in geoscientific research studying soils and the near-surface Earth through multiple disciplines.

## Purpose

This repository provides structured, machine-readable and human-readable markdown files that describe:

- **Personas** — archetypes of practitioners who work in geoscientific research (e.g., field geologist, hydrologist, climate modeler)
- **Skills** — discipline-specific knowledge, tools, and methodologies organized by scientific domain
- **Culture** — shared norms, constraints, and best practices governing how the community conducts open science, manages data, and builds models

These files are designed to be consumed by AI agents (e.g., the GAIA platform) as contextual instructions, and by human contributors as onboarding and reference material.

## Disciplines Covered

| Folder | Discipline |
|--------|-----------|
| `skills/geophysics/` | Applied and exploration geophysics for subsurface characterization |
| `skills/climate-science/` | Climate modelling, forcing datasets, and attribution |
| `skills/hydrology/` | Surface and subsurface water processes |
| `skills/geomorphology/` | Landform evolution and surface processes |
| `skills/geology/` | Stratigraphy, lithology, structural geology |
| `skills/geotechnical-engineering/` | Soil mechanics, foundation engineering, site investigation |
| `skills/ecology/` | Soil-plant-atmosphere interactions and biodiversity metrics |

## Repository Layout

```
gaia-skills/
├── personas/                          # Practitioner archetypes
│   ├── _template.md
│   ├── field-geologist.md
│   ├── data-scientist.md
│   ├── hydrologist.md
│   ├── climate-modeler.md
│   ├── geomorphologist.md
│   ├── geotechnical-engineer.md
│   └── ecologist.md
├── skills/                            # Discipline skill files
│   ├── _template.md
│   ├── geophysics/
│   ├── climate-science/
│   ├── hydrology/
│   ├── geomorphology/
│   ├── geology/
│   ├── geotechnical-engineering/
│   └── ecology/
└── culture/                           # Shared cultural norms
    ├── open-science/
    ├── data-management/
    └── modeling/
```

## Usage

Clone or use this repository as a **GitHub template** to start a new skills library. Add markdown files following the templates in each directory. Files are intentionally plain markdown to remain portable across AI platforms and documentation systems.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on adding new personas, skills, and culture documents.

## License

See [LICENSE](LICENSE).
