---
id: skill-climate-downscaling
title: "Statistical Downscaling of Climate Projections"
discipline: "climate-science"
level: "intermediate"
tags:
  - downscaling
  - CMIP6
  - bias-correction
---

# Statistical Downscaling of Climate Projections

## Overview

Statistical downscaling derives high-resolution local climate variables from coarse-resolution global or regional climate model (GCM/RCM) output. It is essential for producing soil-relevant forcing data (precipitation, temperature, radiation) at spatial scales relevant to catchment hydrology, soil-moisture modelling, and agricultural applications.

## Prerequisites

- Familiarity with NetCDF data format and xarray
- Basic understanding of GCM/RCM output variables (tas, pr, hurs, rsds)
- Python or R environment with relevant libraries installed

## Key Concepts

- **Quantile mapping (QM)**: transfers the CDF of modelled values to match the observed CDF; effective for bias correction of individual variables.
- **Quantile delta mapping (QDM)**: preserves climate change signals while correcting bias; preferred over simple QM for future projections.
- **BCSD (Bias Correction Spatial Disaggregation)**: combines QM with spatial interpolation to produce gridded downscaled products.
- **Perfect prognosis (PP)**: regression-based method linking large-scale predictors to local predictands.

## Tools & Software

| Tool | Version / Source | Purpose |
|------|-----------------|---------|
| Python (xclim, xarray) | Open-source | Bias correction and climate indices |
| R (climate4R, qmap) | Open-source | Statistical downscaling and QM |
| BCSD / MACA | Open datasets | Pre-downscaled climate products |
| Copernicus CDS API | copernicus.eu | ERA5 and CMIP6 data access |

## Step-by-Step Workflow

1. **Access data**: download observational baseline (e.g., ERA5, E-OBS, CHIRPS) and GCM historical and future scenario runs from CMIP6/CDS.
2. **Align grids**: regrid GCM output to observational grid using conservative remapping (CDO: `remapcon`).
3. **Split periods**: define calibration (historical) and evaluation periods.
4. **Fit bias-correction model**: derive transfer function (QDM or QM) using calibration-period data.
5. **Apply correction**: apply transfer function to historical and future GCM output.
6. **Validation**: compare corrected output against withheld observations (KGE, bias, wet-day frequency).
7. **Generate ensemble**: repeat steps 1–6 for multiple GCMs and SSP scenarios to characterise uncertainty.
8. **Archive outputs**: store downscaled NetCDF files with CF-compliant metadata, provenance, and DOI.

## Common Pitfalls

- **Stationarity assumption**: QM assumes the bias structure remains constant into the future — use QDM or ISIMIP methods to preserve delta signals.
- **Variance inflation**: simple mean-bias correction does not correct variance; use distribution-based methods.
- **Precipitation occurrence**: correct wet-day frequency before adjusting intensity to avoid splitting of spurious drizzle.
- **Cross-variable consistency**: downscale temperature and precipitation independently then check thermodynamic consistency.

## Quality Checks

- Evaluate against independent observations using KGE ≥ 0.5 and percent bias <10%.
- Check precipitation extremes (Rx1day, Rx5day) are preserved.
- Verify spatial coherence of downscaled fields.

## References

- Maraun et al. (2017) — Towards process-informed bias correction of climate change simulations, Nature Climate Change
- Cannon, A. J., Sobie, S. R. & Murdock, T. Q. (2015) — Bias Correction of GCM Precipitation by Quantile Mapping, Journal of Climate
- Gudmundsson et al. (2012) — Technical Note: Downscaling RCM precipitation to the station scale using statistical transformations, Hydrology and Earth System Sciences
