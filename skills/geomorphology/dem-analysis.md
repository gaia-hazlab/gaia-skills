---
id: skill-dem-analysis
title: "DEM-Based Geomorphometric Analysis"
discipline: "geomorphology"
level: "beginner"
tags:
  - terrain-analysis
  - DEM
  - hillslope
  - drainage-network
---

# DEM-Based Geomorphometric Analysis

## Overview

Digital Elevation Model (DEM) analysis extracts quantitative terrain attributes (slope, aspect, curvature, flow accumulation) that describe the form and process domains of landscapes. These attributes are fundamental inputs to hydrological, erosion, and landslide models, and to pedogenic studies that link soil properties to topographic position.

## Prerequisites

- Access to a DEM (SRTM, Copernicus DEM, LiDAR-derived, or SfM-derived)
- QGIS, SAGA GIS, or Python (richdem, pysheds, whitebox-tools)
- Basic understanding of coordinate reference systems and raster operations

## Key Concepts

- **Slope**: first derivative of elevation; controls gravitational driving force on material movement and runoff velocity.
- **Aspect**: direction of maximum slope; influences solar radiation, soil moisture, and vegetation.
- **Profile and plan curvature**: second derivatives; control flow convergence/divergence and erosion/deposition tendency.
- **Flow accumulation**: number of upslope cells draining through each cell; proxy for discharge and basis of channel network extraction.
- **Topographic wetness index (TWI)**: ln(A/tan β); predicts soil saturation and runoff generation zones.
- **Relief**: local or regional elevation range; relates to tectonic uplift and erosion rates.

## Tools & Software

| Tool | Version / Source | Purpose |
|------|-----------------|---------|
| QGIS | Open-source | Raster terrain analysis and visualisation |
| SAGA GIS | Open-source | Advanced geomorphometry modules |
| whitebox-tools / WhiteboxGAT | Open-source | Hydrological conditioning and terrain analysis |
| richdem / pysheds | Python, open-source | Scriptable terrain attribute computation |
| GDAL | Open-source | DEM reprojection, mosaicking, and format conversion |

## Step-by-Step Workflow

1. **Obtain and preprocess DEM**: download or generate DEM; check projection, resolution, and vertical datum; mosaic tiles if necessary.
2. **Fill sinks**: remove artefact depressions using priority-flood or Wang & Liu algorithm to ensure hydrological connectivity.
3. **Calculate primary attributes**: compute slope (degrees or percent), aspect, profile curvature, plan curvature, and hillshade.
4. **Delineate drainage network**: compute flow direction (D8 or D-infinity); accumulate flow; extract channels above a threshold accumulation area.
5. **Calculate TWI**: TWI = ln(specific catchment area / tan slope); identify saturated zones and riparian corridors.
6. **Map geomorphic units**: combine terrain attributes with object-based image analysis or threshold-based classification to map hillslopes, valley floors, and ridges.
7. **Export and document**: save outputs in GeoTIFF format with metadata (projection, resolution, source DEM, processing date).

## Common Pitfalls

- **Unfilled sinks**: artefact depressions break flow routing — always condition the DEM before hydrological analysis.
- **Projection mismatch**: slope and curvature values depend on horizontal units; ensure DEM is in a projected (metric) CRS.
- **Resolution artefacts**: coarse DEMs underestimate slope and smooth curvature — choose resolution appropriate to the scale of interest.
- **Vertical datum inconsistency**: when mosaicking multiple tiles, verify they share the same vertical datum.

## Quality Checks

- Visual inspection of hillshade and slope maps for artefacts (striping, tile edges, no-data holes).
- Verify drainage network against known river channel locations.
- Check slope distribution histogram: unrealistic spikes or extremes indicate errors.

## References

- Wilson, J. P. & Gallant, J. C. (eds.) (2000) — Terrain Analysis: Principles and Applications
- Beven, K. J. & Kirkby, M. J. (1979) — A physically based variable contributing area model, Hydrological Sciences Journal
- Lindsay, J. B. (2016) — Whitebox GAT: A case study in geomorphometric analysis, Computers & Geosciences
