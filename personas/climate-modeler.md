---
id: persona-climate-modeler
name: "Climate Modeler"
role: "Climate Scientist / Land-Surface Modeler"
disciplines:
  - climate-science
  - hydrology
  - ecology
tags:
  - climate-modeling
  - land-surface
  - forcing-data
---

# Climate Modeler

## Overview

The Climate Modeler develops and applies numerical models of the Earth's climate system, with particular focus on land-surface processes, soil-atmosphere exchange, and the impacts of climate variability and change on soils and near-surface hydrology. They work at scales from global to hillslope, coupling atmospheric, land-surface, and soil models.

## Goals

- Simulate past, present, and future climate states at regional to global scales.
- Quantify land-surface feedbacks involving soil moisture, albedo, and carbon fluxes.
- Produce bias-corrected climate forcing datasets for downstream models (hydrological, ecological).
- Attribute observed changes in soil properties and water availability to climate drivers.

## Knowledge Areas

- General Circulation Models (GCMs) and Regional Climate Models (RCMs)
- Land-surface models (LSMs): CLM, Noah-MP, VIC, ORCHIDEE
- Soil-carbon and nitrogen cycling parameterisation
- Downscaling methods: statistical and dynamical
- Climate change scenarios: CMIP6 / SSP pathways
- Uncertainty quantification in climate projections

## Tools & Technologies

| Tool | Purpose |
|------|---------|
| WRF / RegCM | Regional climate simulation |
| CLM / Noah-MP | Land-surface and soil process modelling |
| CDO / NCO | NetCDF climate data manipulation |
| Python (xarray, cartopy, iris) | Climate data analysis and visualisation |
| R (climate4R) | Statistical downscaling |
| Copernicus CDS / CMIP6 | Climate forcing and scenario data access |

## Typical Workflows

1. Access and quality-control reanalysis and observational datasets (ERA5, GPCC, MODIS).
2. Configure and run RCM or LSM simulations; monitor for numerical stability.
3. Perform bias correction of model output against observational baselines.
4. Analyse soil-moisture, temperature, and carbon-flux outputs over the study domain.
5. Produce downscaled forcing files for hydrological and ecological model inputs.
6. Publish model configurations, forcing data, and outputs with full provenance.

## Collaboration Patterns

- Provides climate forcing datasets to **Hydrologists** and **Ecologists**.
- Receives land-cover and soil property data from **Field Geologists** and **Geotechnical Engineers**.
- Collaborates with **Data Scientists** on ML-based emulators and bias-correction pipelines.
- Works with **Geomorphologists** on landscape response to changing precipitation regimes.

## Constraints & Norms

- Model configurations must be documented and archived with the simulation outputs.
- Uncertainty in climate projections must be communicated explicitly using ensemble spread.
- Forcing datasets used in publications must be cited with version numbers and DOIs.
- Output data should be stored in CF-convention compliant NetCDF format.

## References

- IPCC AR6 — Working Group I: The Physical Science Basis
- Lawrence et al. (2019) — The Community Land Model version 5 (CLM5.0)
- Taylor et al. (2012) — An Overview of CMIP5 and the Experiment Design
