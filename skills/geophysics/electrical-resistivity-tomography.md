---
id: skill-ert
title: "Electrical Resistivity Tomography (ERT)"
discipline: "geophysics"
level: "intermediate"
tags:
  - subsurface-characterisation
  - near-surface-geophysics
  - soil-moisture
---

# Electrical Resistivity Tomography (ERT)

## Overview

Electrical Resistivity Tomography is a non-invasive near-surface geophysical technique that images the spatial distribution of electrical resistivity in the subsurface. It is widely applied in soil and regolith characterisation, groundwater mapping, landslide investigation, and soil-moisture monitoring. Resistivity contrasts reflect variations in water content, clay content, salinity, and porosity.

## Prerequisites

- Understanding of basic electrical principles (Ohm's law, current flow in heterogeneous media)
- Familiarity with basic field survey procedures
- Python or MATLAB for data processing (or a GUI-based inversion software)

## Key Concepts

- **Apparent resistivity**: the resistivity value measured assuming a homogeneous half-space; used as a data quality indicator before inversion.
- **Electrode array geometry**: Wenner, Schlumberger, dipole-dipole, and gradient configurations each offer different depth sensitivity and lateral resolution trade-offs.
- **Inversion**: converting apparent resistivity pseudo-sections into true resistivity models using regularised least-squares minimisation.
- **Resolution and depth of investigation**: approximately one-fifth to one-sixth of the maximum electrode spread.

## Tools & Software

| Tool | Version / Source | Purpose |
|------|-----------------|---------|
| RES2DINV / RES3DINV | Commercial (Geotomo) | 2D/3D ERT inversion |
| pyGIMLi | Open-source (pygimli.org) | Open Python-based ERT modelling and inversion |
| ResIPy | Open-source (GitHub) | GUI-based 2D/3D ERT inversion wrapper |
| ABEM / AGM / Syscal | Hardware | Multi-electrode resistivity meters |

## Step-by-Step Workflow

1. **Survey design**: choose electrode spacing (Δx) and array type based on target depth and resolution requirements. For soil profiles, Δx = 0.25–2 m is typical.
2. **Electrode deployment**: lay out electrode cable; insert electrodes to consistent depth; measure contact resistance for all electrodes (<1 kΩ ideal).
3. **Data acquisition**: run automated sequence; record apparent resistivity, standard deviation of repeated measurements, and reciprocal errors.
4. **Quality control**: remove data points with reciprocal error >5%; flag electrodes with contact resistance >5 kΩ.
5. **Inversion**: import data into inversion software; set regularisation parameter (λ) and mesh resolution; run inversion to RMS ≤5%.
6. **Interpretation**: correlate resistivity model with borehole logs, soil profiles, or other geophysical data.
7. **Output and archiving**: export inverted model in open format (e.g., VTK); archive raw data, processing scripts, and metadata.

## Common Pitfalls

- **High contact resistance**: use water or bentonite to improve coupling; repeat measurements.
- **Cultural noise**: metal fences, buried pipes, and power lines can introduce artefacts — note their locations and flag affected data.
- **Inappropriate regularisation**: over-smoothing obscures thin layers; under-smoothing produces artefacts. Perform an L-curve analysis to select λ.
- **Topographic distortion**: always apply topographic correction when surface relief >5% of profile length.

## Quality Checks

- Reciprocal error mean <2%, maximum <5%.
- Inversion RMS misfit ≤5%.
- Correlation of resistivity boundaries with borehole or soil pit data where available.
- Sensitivity analysis: compute data coverage / sensitivity maps and mask low-sensitivity zones.

## Example Outputs

- 2D resistivity cross-sections showing soil layer boundaries and water-table depth.
- Time-lapse ERT difference sections tracking soil-moisture change during rainfall events.
- 3D resistivity volumes for site-scale subsurface characterisation.

## References

- Loke, M. H. (2004) — Tutorial: 2-D and 3-D electrical imaging surveys (available at https://www.geotomosoft.com)
- Kemna et al. (2012) — An overview of the spectral induced polarization method for near-surface applications, Near Surface Geophysics
- Binley, A. & Slater, L. (2020) — Resistivity and Induced Polarization: Theory and Applications to the Near-Surface Earth
