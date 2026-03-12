---
id: skill-cpt
title: "Cone Penetration Testing (CPT) Interpretation"
discipline: "geotechnical-engineering"
level: "intermediate"
tags:
  - site-investigation
  - in-situ-testing
  - soil-classification
  - liquefaction
---

# Cone Penetration Testing (CPT) Interpretation

## Overview

The Cone Penetration Test advances a standardised instrumented probe into the ground at a constant rate and continuously measures tip resistance (qc), sleeve friction (fs), and pore-water pressure (u2). CPT data provide high-resolution continuous soil profiling, classification, and derivation of engineering properties without sample retrieval. It is the most efficient in-situ test for soil characterisation in geotechnical and geohazard investigations.

## Prerequisites

- Basic knowledge of soil mechanics (effective stress, shear strength, consolidation)
- Familiarity with CPT equipment and standards (ISO 22476-1, ASTM D5778)
- Python or R for data processing, or a commercial CPT interpretation package

## Key Concepts

- **Corrected tip resistance (qt)**: qc corrected for unequal end area effects using pore pressure: qt = qc + u2(1−a).
- **Normalised cone resistance (Qt)** and **friction ratio (Fr)**: dimensionless parameters used in soil behaviour type (SBT) classification.
- **Soil Behaviour Type (SBT) chart**: Robertson (1990/2016) chart classifies soils from sensitive fine-grained (Zone 1) to coarse-grained (Zone 7) using Qt and Fr.
- **Ic (SBT index)**: single index combining Qt and Fr for automated classification; Ic > 2.6 typically indicates fine-grained soil.
- **Liquefaction triggering**: CPT-based simplified procedure (Youd et al. 2001; Robertson & Cabal 2022) estimates cyclic resistance ratio (CRR) from qc1N.

## Tools & Software

| Tool | Version / Source | Purpose |
|------|-----------------|---------|
| CPTSPY | Open-source (GitHub) | Python CPT data parsing and classification |
| CLiq / NovoLIQ | Commercial | Liquefaction assessment |
| GeoLogger / Python (pandas) | Open-source | CPT data handling |
| gINT | Commercial | CPT log management and plotting |

## Step-by-Step Workflow

1. **Check raw data quality**: verify push rate (≈2 cm/s ± 25%), zero-load readings, and calibration records.
2. **Apply area correction**: compute qt from qc and u2 using the probe area ratio (a) from calibration certificate.
3. **Calculate derived parameters**: compute Rf = (fs/qt)×100, Qt, Fr, and Bq; apply stress normalisation.
4. **Classify soil behaviour type**: plot Qt vs Fr on Robertson SBT chart; assign Ic value to each depth increment.
5. **Derive engineering properties**: estimate undrained shear strength (su = (qt − σv)/Nkt), friction angle, relative density, and OCR as appropriate.
6. **Perform liquefaction assessment** (where required): calculate CSR, CRR, and FS against liquefaction; map liquefaction potential index (LPI).
7. **Present results**: plot qc, fs, u2, Rf, and SBT log vs depth; export in open format (CSV, AGS4).

## Common Pitfalls

- **Pore-pressure saturation**: u2 sensor must be fully saturated before testing in low-permeability soils — use glycerine or silicon oil.
- **Rate effects**: pushing faster than 2 cm/s in partially drained materials inflates qc — maintain constant rate.
- **Shallow refusal**: dense layers near surface can prevent penetration; use pre-bored casing or alternative test.
- **Incorrect Nkt factor**: su derived from qt is sensitive to the cone factor; calibrate against laboratory tests where possible.

## Quality Checks

- Zero readings before and after each push within ±2% of measurement range.
- Push rate log should show ≤25% deviation from 20 mm/s.
- Monotonic pore pressure response in soft clay (Bq > 0); erratic u2 in granular soils is expected.
- Cross-check classification against adjacent borehole logs.

## References

- Robertson, P. K. (2016) — Cone penetration test (CPT)-based soil behaviour type (SBT) classification system — an update, Canadian Geotechnical Journal
- ISO 22476-1:2022 — Field testing: Electrical cone and piezocone penetration tests
- Youd et al. (2001) — Liquefaction Resistance of Soils: Summary Report from the 1996 NCEER and 1998 NCEER/NSF Workshops, Journal of Geotechnical and Geoenvironmental Engineering
