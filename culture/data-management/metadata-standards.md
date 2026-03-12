---
id: culture-data-management-metadata
category: "data-management"
title: "Metadata Standards for Geoscientific Field and Laboratory Data"
tags:
  - metadata
  - field-data
  - laboratory-data
  - standards
---

# Metadata Standards for Geoscientific Field and Laboratory Data

## Purpose

Comprehensive metadata is what transforms a raw data file into a reusable scientific asset. This document defines the minimum metadata requirements for field observations, geophysical surveys, laboratory analyses, and sensor time series produced in this community. These standards ensure that data can be correctly interpreted, reproduced, and integrated with other datasets years after collection.

## Scope

All field and laboratory datasets, including soil profiles, borehole logs, geophysical surveys, water-quality analyses, and time-series from monitoring stations.

## Requirements

### Universal fields (all data types)
- [ ] **Dataset title**: descriptive, unique, and human-readable.
- [ ] **Creator(s)**: name(s) and ORCID(s) of data collectors and responsible scientists.
- [ ] **Creation date**: ISO 8601 date or date range of data collection.
- [ ] **Geographic location**: coordinate bounding box (WGS84) or site identifier with coordinates; include spatial resolution.
- [ ] **Temporal coverage**: start and end datetime in UTC.
- [ ] **Licence**: machine-readable SPDX identifier (e.g., `CC-BY-4.0`).
- [ ] **Related publication**: DOI of any associated paper.
- [ ] **Funding**: grant number and funding agency.

### Spatial data
- [ ] Coordinate Reference System (CRS): EPSG code and description.
- [ ] Horizontal accuracy (m) and vertical datum.
- [ ] Spatial resolution or sampling interval.

### Time-series / sensor data
- [ ] Sensor type, manufacturer, and model.
- [ ] Measurement frequency and aggregation method.
- [ ] Calibration date and certificate reference.
- [ ] Quality flag codes and their definitions.

### Laboratory analytical data
- [ ] Sample ID linked to field collection metadata.
- [ ] Analytical method (e.g., ISO standard number, published protocol).
- [ ] Laboratory and instrument identifier.
- [ ] Detection limits and units.
- [ ] Reference material results and acceptance criteria.

## Recommended Practices

- Use a community metadata template (e.g., PANGAEA template, ISO 19115 profile, EML) when submitting to a repository.
- Store metadata in a sidecar file alongside each data file (`dataset_metadata.json` or `README.txt`) before final archiving.
- Assign internal sample IDs at the time of collection; do not rename samples post-collection.
- Keep a field logbook (digital or paper) and scan/photograph it as part of the archival package.

## Anti-Patterns to Avoid

- Recording only decimal degree coordinates without a stated geodetic datum (WGS84 vs. local datum can differ by metres to hundreds of metres).
- Using ambiguous date formats (e.g., 03/04/22) — always use ISO 8601.
- Describing analytical methods as "standard laboratory procedures" without an explicit citation.
- Omitting detection limits for geochemical or environmental data.

## Tools & Resources

| Resource | Purpose |
|----------|---------|
| PANGAEA metadata template | Community standard for geoscience data |
| ISO 19115 | Geographic information metadata standard |
| EML (Ecological Metadata Language) | Ecology and environmental data metadata |
| Dublin Core | Lightweight general-purpose metadata |
| schema.org Dataset | Web-discoverable dataset metadata |
| re3data.org | Registry of research data repositories |

## References

- ISO 19115-1:2014 — Geographic information: Metadata
- Jones, M. B. et al. (2019) — Ecological Metadata Language version 2.2.0, KNB Data Repository
- PANGAEA — Publisher for Earth and Environmental Science Data (https://www.pangaea.de)
