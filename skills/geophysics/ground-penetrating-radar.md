---
id: skill-gpr
title: "Ground-Penetrating Radar (GPR) for Soil Investigation"
discipline: "geophysics"
level: "intermediate"
tags:
  - subsurface-characterisation
  - near-surface-geophysics
  - soil-stratigraphy
---

# Ground-Penetrating Radar (GPR) for Soil Investigation

## Overview

Ground-Penetrating Radar uses high-frequency electromagnetic pulses (10 MHz–2.6 GHz) to image dielectric contrasts in the shallow subsurface. In soil investigation it reveals stratigraphic horizons, discontinuities, roots, soil-moisture variations, and buried objects. GPR is fast to deploy, non-destructive, and provides continuous profiles, making it complementary to ERT and intrusive borehole methods.

## Prerequisites

- Basic understanding of electromagnetic wave propagation
- Familiarity with common data formats (DZT, DT1, SEG-Y)
- Access to GPR processing software

## Key Concepts

- **Frequency vs. depth trade-off**: lower-frequency antennas (50–200 MHz) penetrate deeper but offer lower resolution; higher-frequency antennas (400 MHz–2.6 GHz) resolve thin layers but attenuate rapidly in conductive (clay-rich or wet) soils.
- **Two-way travel time (TWTT)**: the time for the radar pulse to travel to a reflector and return; converted to depth using the electromagnetic wave velocity in the medium.
- **Common midpoint (CMP) survey**: used to estimate subsurface wave velocity and convert TWTT to depth.
- **Dielectric permittivity**: the primary control on wave velocity; strongly influenced by soil-water content (Topp's equation links volumetric water content to permittivity).

## Tools & Software

| Tool | Version / Source | Purpose |
|------|-----------------|---------|
| GSSI SIR / MALA ProEx / Sensors & Software pulseEKKO | Hardware | GPR data acquisition |
| ReflexW | Commercial (Sandmeier) | GPR data processing and interpretation |
| GPRPy | Open-source (GitHub) | Python-based GPR processing and visualisation |
| OpendTect | Open-source | 3D GPR volume interpretation |

## Step-by-Step Workflow

1. **Survey design**: select antenna frequency based on target depth and resolution; plan line spacing for 2D grid or 3D survey.
2. **Calibration**: conduct CMP survey or use known reflector depths to estimate wave velocity.
3. **Data acquisition**: set time window (>2× target TWTT); record GPS coordinates; maintain consistent antenna spacing and orientation.
4. **Pre-processing**: apply time-zero correction, dewow filter, bandpass filter, and background subtraction.
5. **Velocity analysis**: derive depth-velocity model from CMP gathers or hyperbola fitting.
6. **Migration**: apply Kirchhoff or FK migration to collapse diffractions and correctly position reflectors.
7. **Interpretation**: pick horizon reflectors; convert TWTT to depth; correlate with borehole or soil pit data.
8. **Archiving**: store raw data, processing parameter files, and velocity model with metadata.

## Common Pitfalls

- **High soil conductivity**: clay-rich or saline soils attenuate signals rapidly — check expected penetration depth before fieldwork.
- **Ringing and multiples**: strong surface reflections can mask shallow features; apply dewow and subtract mean trace.
- **Incorrect velocity**: errors in velocity estimation directly propagate to depth errors; validate against independent depth control.
- **Environmental interference**: metallic structures, wire fences, and radio interference can produce artefacts — note locations in field log.

## Quality Checks

- Verify time-zero pick is consistent across all traces.
- Validate velocity model against at least one borehole or direct excavation.
- Check that migrated data does not over-collapse or under-collapse diffractions.
- Record and report signal-to-noise ratio and maximum interpretable depth.

## References

- Jol, H. M. (ed.) (2009) — Ground Penetrating Radar Theory and Applications
- Neal, A. (2004) — Ground-penetrating radar and its use in sedimentology, Earth-Science Reviews
- Topp, G. C., Davis, J. L. & Annan, A. P. (1980) — Electromagnetic determination of soil water content, Water Resources Research
