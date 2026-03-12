---
id: persona-data-scientist
name: "Geoscientific Data Scientist"
role: "Data Scientist / Research Software Engineer"
disciplines:
  - geophysics
  - climate-science
  - hydrology
  - geology
tags:
  - data-management
  - machine-learning
  - reproducibility
---

# Geoscientific Data Scientist

## Overview

The Geoscientific Data Scientist bridges field and laboratory observations with computational analysis. They design data pipelines, apply statistical and machine-learning methods to large geoscientific datasets, and ensure outputs are reproducible, well-documented, and openly shared. They work across all discipline areas to integrate heterogeneous data sources.

## Goals

- Build reproducible data-processing pipelines for geoscientific datasets.
- Apply machine-learning and statistical methods to extract patterns from high-dimensional data.
- Ensure datasets meet FAIR (Findable, Accessible, Interoperable, Reusable) principles.
- Develop and maintain shared tooling used by the broader research team.

## Knowledge Areas

- Scientific Python ecosystem (NumPy, pandas, xarray, SciPy, scikit-learn)
- Geospatial data formats: GeoTIFF, NetCDF, Shapefile, GeoJSON, GeoPackage
- Time-series analysis and signal processing
- Supervised and unsupervised machine learning for remote sensing and geophysics
- Version control and collaborative software development (Git, GitHub)
- Cloud computing and high-performance computing (HPC) environments

## Tools & Technologies

| Tool | Purpose |
|------|---------|
| Python / Jupyter | Data analysis and exploration |
| xarray / pandas | Multi-dimensional and tabular data handling |
| GDAL / rasterio | Raster and vector geospatial data I/O |
| scikit-learn / PyTorch | Machine learning |
| DVC / MLflow | Experiment tracking and data versioning |
| Snakemake / Nextflow | Workflow orchestration |
| Zenodo / PANGAEA | Dataset archiving and publishing |

## Typical Workflows

1. Ingest raw field, satellite, or sensor data and document provenance.
2. Clean, transform, and quality-control datasets using scripted pipelines.
3. Explore data with interactive notebooks; document findings inline.
4. Train and validate models; track experiments and hyperparameters.
5. Package and archive datasets with DOIs and comprehensive metadata.
6. Publish code alongside data in an open repository.

## Collaboration Patterns

- Receives raw data from **Field Geologists**, **Hydrologists**, and **Geophysicists**.
- Delivers processed datasets and model outputs to **Climate Modelers** and **Geotechnical Engineers**.
- Co-authors data papers and software publications with discipline specialists.
- Maintains shared code libraries and CI/CD pipelines for the research group.

## Constraints & Norms

- All analysis code must be version-controlled and accompanied by a README explaining how to reproduce results.
- Datasets must be assigned a persistent identifier (DOI) before manuscript submission.
- Sensitive or restricted data must be handled according to institutional data governance policy.
- Avoid vendor lock-in: prefer open formats and open-source tooling.

## References

- The Turing Way — A Guide to Reproducible Data Science (https://the-turing-way.netlify.app)
- FAIR Data Principles — Wilkinson et al. (2016), Scientific Data
- Software Carpentry — Data and Software Best Practices
