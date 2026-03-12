---
id: culture-open-science-principles
category: "open-science"
title: "Open Science Principles for Geoscientific Research"
tags:
  - open-access
  - reproducibility
  - transparency
  - FAIR
---

# Open Science Principles for Geoscientific Research

## Purpose

Open science ensures that geoscientific knowledge, data, and methods are freely accessible, transparent, and reproducible. These principles apply to all practitioners in this community — from field data collectors to modellers — and form the baseline cultural expectations for contributing to and using shared resources in soil and near-surface Earth research.

## Principles

1. **Openness by default**: data, code, and publications should be open unless there is a specific, documented reason otherwise (legal, commercial, or safety constraint).
2. **Reproducibility**: all analyses and model outputs must be reproducible by an independent researcher following documented methods and using archived data and code.
3. **Transparency**: methods, assumptions, uncertainties, and limitations must be fully disclosed.
4. **Attribution and citation**: all data, software, and ideas used must be properly cited; contributors must receive appropriate credit.
5. **Inclusivity**: open science should lower barriers to participation and knowledge sharing across career stages, institutions, and geographies.

## Requirements

- [ ] Publish datasets in open repositories (e.g., Zenodo, PANGAEA, Hydroshare) with DOIs before or upon manuscript submission.
- [ ] Archive all analysis code in a public version-controlled repository (e.g., GitHub) linked to the publication.
- [ ] Use open, non-proprietary data formats (NetCDF, GeoJSON, CSV, GeoTIFF) as primary exchange formats.
- [ ] Provide a machine-readable data licence (e.g., CC BY 4.0, CC0) for all published datasets.
- [ ] Document software dependencies and versions in a machine-readable environment file (e.g., `environment.yml`, `requirements.txt`, `renv.lock`).
- [ ] Register pre-registration or data management plans with the funding agency or an open registry where required.

## Recommended Practices

- Post preprints to EarthArXiv, ESSOAr, or arXiv before or alongside journal submission.
- Use ORCID identifiers to unambiguously attribute authorship.
- Include a README and a CITATION.cff file in every code repository.
- Choose journals and conferences that support open-access publication (Plan S compliant where possible).
- Conduct open peer review where the journal/platform supports it.
- Use containerisation (Docker, Singularity/Apptainer) to maximise long-term reproducibility.

## Anti-Patterns to Avoid

- Sharing data only "upon reasonable request" — this is not open science.
- Placing analysis code in supplementary PDFs rather than executable repositories.
- Using proprietary binary formats as the sole output format.
- Describing methods only in prose without accompanying code or detailed protocols.
- Citing data without version or access date, making the citation unresolvable.

## Tools & Resources

| Resource | Purpose |
|----------|---------|
| Zenodo | General-purpose open data and code archiving with DOI |
| PANGAEA | Geoscientific and oceanographic data publisher |
| HydroShare | Hydrology data and model sharing |
| EarthArXiv | Earth science preprint server |
| ORCID | Persistent researcher identifier |
| GitHub / GitLab | Code hosting and version control |
| Licenses (CC BY 4.0, MIT, Apache 2.0) | Open content and software licensing |

## References

- Wilkinson et al. (2016) — The FAIR Guiding Principles for scientific data management and stewardship, Scientific Data
- Vicente-Saez & Martinez-Fuentes (2018) — Open Science now: A systematic literature review, Journal of Business Research
- Stall et al. (2019) — Make scientific data FAIR, Nature
