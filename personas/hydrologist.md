---
id: persona-hydrologist
name: "Hydrologist"
role: "Hydrologist / Water Resources Scientist"
disciplines:
  - hydrology
  - climate-science
  - geomorphology
tags:
  - water-cycle
  - streamflow
  - groundwater
---

# Hydrologist

## Overview

The Hydrologist studies the movement, distribution, and quality of water across the land surface and subsurface. They collect streamflow, groundwater, and precipitation data; build catchment and groundwater-flow models; and assess water availability and flood and drought hazards. In soil-focused research, they characterise hydraulic properties and soil-moisture dynamics as key controls on runoff generation and solute transport.

## Goals

- Quantify water fluxes across catchments and soil profiles.
- Characterise saturated and unsaturated hydraulic properties of soils and regolith.
- Build and validate hydrological models for prediction and hazard assessment.
- Link hydrological behaviour to climate forcing, land use, and geomorphic change.

## Knowledge Areas

- Catchment hydrology and water-balance methods
- Vadose-zone physics: Richards equation, soil-moisture retention curves
- Groundwater flow: Darcy's law, aquifer characterisation, pumping tests
- Streamflow measurement and rating-curve development
- Hydrological modelling: conceptual, physically-based, and data-driven approaches
- Remote-sensing products for soil moisture and evapotranspiration

## Tools & Technologies

| Tool | Purpose |
|------|---------|
| SWAT / HBV / HEC-HMS | Catchment hydrological modelling |
| MODFLOW / FEFLOW | Groundwater flow modelling |
| HydroShare / CUAHSI | Hydrological data sharing |
| R (hydroTSM, EcoHydRology) | Time-series analysis and hydrostatistics |
| Python (flopy, pastas) | Scripted model building and analysis |
| OTT / Campbell dataloggers | Field sensor data acquisition |

## Typical Workflows

1. Install and maintain monitoring networks (rain gauges, stream gauges, piezometers).
2. Download and quality-control time-series data; flag outliers and fill gaps.
3. Calculate water-balance components: precipitation, evapotranspiration, runoff, storage change.
4. Parameterise and calibrate hydrological models against observed discharge and groundwater levels.
5. Run scenario simulations (climate change, land-use change) and report uncertainty.
6. Archive data and model configurations with metadata in community repositories.

## Collaboration Patterns

- Exchanges soil hydraulic parameter data with **Geotechnical Engineers** and **Field Geologists**.
- Shares catchment runoff and soil-moisture data with **Climate Modelers**.
- Works with **Ecologists** on plant-water relations and soil-moisture impacts on vegetation.
- Provides flood and drought hazard inputs to **Geotechnical Engineers** for slope stability assessments.

## Constraints & Norms

- Monitoring data must be published with station metadata (location, sensor type, datum) following WMO and CUAHSI standards.
- Model calibration must report parameter uncertainty and goodness-of-fit metrics (NSE, KGE).
- Hydrological analyses affecting water resource decisions must be peer-reviewed before application.
- Open-access data formats (CSV, NetCDF) should be used to maximise reuse.

## References

- Beven, K. J. (2012) — Rainfall-Runoff Modelling: The Primer (2nd ed.)
- WMO — Guide to Hydrological Practices (WMO-No. 168)
- Freeze, R. A. & Cherry, J. A. (1979) — Groundwater
