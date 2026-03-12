---
id: culture-data-management-fair
category: "data-management"
title: "FAIR Data Practices for Geoscientific Datasets"
tags:
  - FAIR
  - metadata
  - data-publishing
  - interoperability
---

# FAIR Data Practices for Geoscientific Datasets

## Purpose

The FAIR principles (Findable, Accessible, Interoperable, Reusable) provide a framework for managing and publishing geoscientific data so that it can be discovered, understood, and reused by humans and machines. Adherence to FAIR practices is a cultural requirement for all data produced in this research community.

## Scope

Applies to all geoscientific datasets produced in this community, including field observations, geophysical surveys, laboratory analyses, model inputs, and model outputs.

## Requirements

### Findable
- [ ] Assign a globally unique, persistent identifier (DOI via Zenodo, PANGAEA, or equivalent) to every published dataset.
- [ ] Include rich, machine-readable metadata (ISO 19115, Dublin Core, or discipline-specific schema) with every dataset.
- [ ] Register datasets in a searchable index or catalogue (PANGAEA, IEDA, HydroShare, Copernicus CAMS).

### Accessible
- [ ] Store data in an openly accessible repository with a clear access protocol (HTTPS, API).
- [ ] Apply an explicit open licence (CC BY 4.0, CC0) or document access restrictions with contact information.
- [ ] Metadata must remain accessible even if the dataset itself is restricted or embargoed.

### Interoperable
- [ ] Use open, community-standard data formats: NetCDF (CF conventions), GeoTIFF, GeoJSON, CSV, or AGS4.
- [ ] Use controlled vocabularies and ontologies for parameter names: CF standard names, SWEET, ENVO.
- [ ] Provide explicit coordinate reference system (CRS) and vertical datum information for all spatial data.

### Reusable
- [ ] Provide a detailed data description: collection method, instrument, calibration, processing steps, and quality flags.
- [ ] Include provenance: link raw and derived datasets; document all transformations.
- [ ] Describe data quality: completeness, accuracy, and known limitations.
- [ ] Ensure software used for data processing is also published and citable.

## Recommended Practices

- Create and maintain a Data Management Plan (DMP) from the start of each project using a tool such as DMPonline or RDMO.
- Follow a consistent file-naming convention: `YYYYMMDD_site_instrument_variable_version.ext`.
- Maintain a README file alongside each dataset describing the file structure and variable definitions.
- Use ISO 8601 (YYYY-MM-DD HH:MM:SS UTC) for all date-time fields.
- Flag and document outliers and missing values explicitly (e.g., NaN, −9999 with explanation in metadata).

## Anti-Patterns to Avoid

- Storing primary data only on local hard drives or shared drives without backup or version control.
- Publishing datasets without variable units, coordinate reference systems, or collection dates.
- Using proprietary formats (XLSX, .mat, .accdb) as the sole distribution format.
- Mixing data collection and data processing in undocumented manual steps.
- Embargoing datasets without a defined end date or data access procedure.

## Tools & Resources

| Resource | Purpose |
|----------|---------|
| Zenodo | General-purpose FAIR data archiving with DOI |
| PANGAEA | Geoscientific and environmental data publisher |
| HydroShare | Hydrological data and model sharing |
| GFZ Data Services | Geoscientific data with DOI |
| IEDA EarthChem | Geochemical data archiving |
| DMPonline | Data Management Plan creation |
| ORCID | Persistent researcher identifier for data attribution |
| CF Conventions | Standard names and metadata for NetCDF |

## References

- Wilkinson et al. (2016) — The FAIR Guiding Principles for scientific data management and stewardship, Scientific Data
- ISO 19115-1:2014 — Geographic information: Metadata — Fundamentals
- GO FAIR Initiative — FAIR Principles (https://www.go-fair.org/fair-principles/)
