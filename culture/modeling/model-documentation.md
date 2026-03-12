---
id: culture-modeling-documentation
category: "modeling"
title: "Model Documentation Practices"
tags:
  - model-documentation
  - transparency
  - reproducibility
  - configuration-management
---

# Model Documentation Practices

## Purpose

Geoscientific models are scientific instruments. Their outputs are only as trustworthy as their documentation. This document defines the minimum documentation requirements for numerical models used in soil, hydrological, geophysical, and climate research within this community. Good model documentation enables others to understand, reproduce, and critically evaluate model results.

## Scope

Applies to all numerical models: process-based, data-driven, statistical, and hybrid models used to simulate or predict geoscientific processes.

## Requirements

- [ ] Every model application must have a **model description document** (or README) that includes:
  - Model name, version, and source (DOI or URL).
  - Governing equations or conceptual basis.
  - Spatial and temporal domain and resolution.
  - Boundary and initial conditions.
  - Parameter values and sources.
  - Forcing data used (name, version, time period, DOI).
- [ ] All configuration files, parameter files, and input data references must be archived in a version-controlled repository.
- [ ] Model code (if modified from a published version) must be forked, version-tagged, and published with a DOI.
- [ ] A **simulation log** must record each model run: date, operator, input file checksums or DOIs, software version, and computing environment.

## Recommended Practices

- Follow the DREAM protocol (Documenting, Reporting and Evaluating a Model) or equivalent community standard.
- Provide schematic diagrams of the model structure and data flow.
- Document the computational environment: OS, compiler, MPI version, or Python/R environment specification.
- Include a "known limitations" section in every model documentation file.
- Register the model in a community model registry (e.g., CSDMS Model Repository, CoMSES Net).

## Anti-Patterns to Avoid

- Referring to model parameters as "default" without specifying the default value and its source.
- Publishing model results without specifying the exact model version used.
- Modifying the model source code without version control, making the run irreproducible.
- Providing only a journal paper reference as model documentation without an archive of the configuration files.

## Tools & Resources

| Resource | Purpose |
|----------|---------|
| CoMSES Net / OpenABM | Model registry for social and geoscientific models |
| CSDMS Model Repository | Community Surface Dynamics Modelling System registry |
| Zenodo | Code and configuration archiving with DOI |
| Git / GitHub | Version control for model code and configuration |
| Snakemake / Nextflow | Automated model workflow management |
| ESMValTool | Evaluation and documentation of climate model output |

## References

- Schmolke et al. (2010) — Mechanistic effect models for ecological risk assessment of chemicals: a state-of-the-art review, Ecological Applications
- Refsgaard & Henriksen (2004) — Modelling guidelines — terminology and guiding principles, Advances in Water Resources
- CSDMS — Model metadata and documentation standards (https://csdms.colorado.edu)
