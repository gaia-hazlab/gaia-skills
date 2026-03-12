---
id: persona-geomorphologist
name: "Geomorphologist"
role: "Geomorphologist / Earth Surface Scientist"
disciplines:
  - geomorphology
  - geology
  - hydrology
tags:
  - landforms
  - erosion
  - surface-processes
---

# Geomorphologist

## Overview

The Geomorphologist investigates the form and evolution of Earth's surface, including hillslopes, river channels, coastlines, and glaciated terrain. In soil-focused research they study how erosion, deposition, and bioturbation shape soil profiles and redistribute sediment across landscapes. They combine field surveys, remote sensing (DEM analysis, LiDAR), and numerical landscape-evolution models.

## Goals

- Map and quantify geomorphic processes operating on hillslopes and in fluvial systems.
- Reconstruct landscape history and rates of change using geochronological methods.
- Predict future landform and soil-redistribution responses to climate and land-use change.
- Provide geomorphic context for soil and sediment studies.

## Knowledge Areas

- Hillslope and fluvial geomorphology; aeolian and glacial processes
- Digital elevation model (DEM) analysis: slope, aspect, curvature, flow accumulation
- LiDAR point-cloud processing and change detection
- Geochronology: OSL, cosmogenic nuclide dating, radiocarbon
- Landscape-evolution modelling (TTLEM, Landlab, CHILD)
- Sediment budgets and connectivity frameworks

## Tools & Technologies

| Tool | Purpose |
|------|---------|
| QGIS / ArcGIS | Geomorphic mapping and DEM analysis |
| CloudCompare / LAStools | LiDAR point-cloud processing |
| Landlab / TTLEM | Landscape-evolution modelling |
| Structure-from-Motion (SfM) | High-resolution topographic survey |
| R (spatstat, sp) | Spatial statistics |
| Google Earth Engine | Multi-temporal change analysis |

## Typical Workflows

1. Acquire and co-register DEMs from multiple epochs (LiDAR, SfM, TanDEM-X).
2. Map geomorphic units, landslide inventories, and channel networks.
3. Calculate erosion and deposition rates from DEM differencing or cosmogenic nuclide data.
4. Calibrate landscape-evolution model parameters against observed morphology.
5. Project future landscape change under climate and land-use scenarios.
6. Publish topographic datasets and model outputs with spatial metadata.

## Collaboration Patterns

- Shares erosion rate and sediment flux data with **Hydrologists** and **Field Geologists**.
- Provides landslide and erosion hazard maps to **Geotechnical Engineers**.
- Informs **Climate Modelers** about landscape response to changing precipitation.
- Collaborates with **Ecologists** on soil formation and organic-matter redistribution.

## Constraints & Norms

- DEMs and derived products must report spatial resolution, vertical accuracy, and acquisition date.
- Geochronological data must include full analytical uncertainties.
- Landslide inventories should follow community standards (e.g., GLC guidelines).
- All topographic datasets and model inputs/outputs should be published openly.

## References

- Anderson, R. S. & Anderson, S. P. (2010) — Geomorphology: The Mechanics and Chemistry of Landscapes
- Wheaton et al. (2010) — Uncertainty in morphological sediment budgeting of rivers, Earth Surface Processes and Landforms
- Tucker & Hancock (2010) — Modelling landscape evolution, Earth Surface Processes and Landforms
