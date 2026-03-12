---
id: skill-catchment-water-balance
title: "Catchment Water Balance Analysis"
discipline: "hydrology"
level: "beginner"
tags:
  - water-balance
  - evapotranspiration
  - runoff
---

# Catchment Water Balance Analysis

## Overview

The catchment water balance partitions incoming precipitation into evapotranspiration, runoff, and changes in storage (soil moisture and groundwater). It is the fundamental accounting framework in hydrology and a prerequisite for all hydrological modelling and water resource assessment. For soil-focused research it quantifies how much water infiltrates, is retained in soil, or becomes deep drainage.

## Prerequisites

- Time-series of precipitation and streamflow at catchment scale
- Familiarity with pandas or R for time-series analysis
- Basic understanding of the hydrological cycle

## Key Concepts

- **Water balance equation**: P = Q + ET + ΔS, where P = precipitation, Q = streamflow, ET = evapotranspiration, ΔS = change in storage.
- **Runoff ratio (Q/P)**: fraction of precipitation that becomes streamflow; sensitive to soil permeability, land cover, and antecedent moisture.
- **Budyko framework**: relates long-term Q/P to the aridity index (PET/P) to benchmark observed catchment behaviour.
- **Potential vs. actual ET**: PET is energy-limited maximum ET; actual ET is constrained by soil-water availability.

## Tools & Software

| Tool | Version / Source | Purpose |
|------|-----------------|---------|
| Python (pandas, numpy) | Open-source | Time-series handling and computation |
| R (hydroTSM, HydroGOF) | Open-source | Hydrological time-series analysis |
| FAO-56 / Penman-Monteith | Method | Reference ET calculation |
| GLEAM / MODIS ET | Remote sensing | Actual ET estimation |

## Step-by-Step Workflow

1. **Compile inputs**: collect daily or sub-daily precipitation, streamflow, temperature, and radiation data; check for gaps and outliers.
2. **Calculate PET**: apply Penman-Monteith or Hargreaves equation using available meteorological data.
3. **Define catchment area**: delineate catchment boundary from DEM (e.g., using pysheds or SAGA GIS); compute area for converting streamflow volume to depth.
4. **Compute annual water balance**: sum P, Q, and estimate ET = P − Q for multi-year periods to minimise storage term.
5. **Estimate storage change (ΔS)**: use GRACE satellite data or groundwater level records for inter-annual ΔS.
6. **Plot Budyko curve**: compare observed Q/P vs PET/P against Budyko envelope to identify anomalies.
7. **Report and archive**: tabulate water balance components with uncertainty ranges; deposit data and scripts in an open repository.

## Common Pitfalls

- **Catchment boundary mismatch**: surface and groundwater divides may differ — check for inter-catchment groundwater transfers.
- **Missing data**: gaps in precipitation records bias the water balance; use ensemble gap-filling methods and report uncertainty.
- **Short record length**: storage fluctuations can dominate annual balances; use ≥10-year records for robust long-term averages.
- **Gauge undercatch**: rain gauges underestimate precipitation, especially at high wind speeds; apply correction factors.

## Quality Checks

- Annual Q/P should fall within climatically expected range (0–1); values >1 indicate data errors or groundwater import.
- Plot cumulative double-mass curve of P vs. Q to detect trend changes or data inconsistencies.
- Verify catchment area from DEM against published values.

## References

- Budyko, M. I. (1974) — Climate and Life, Academic Press
- Allen et al. (1998) — Crop evapotranspiration: Guidelines for computing crop water requirements, FAO Irrigation and Drainage Paper 56
- Müller Schmied et al. (2021) — Variations of global and continental water balance components as impacted by climate forcing uncertainty, Hydrology and Earth System Sciences
