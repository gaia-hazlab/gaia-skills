---
id: culture-modeling-validation
category: "modeling"
title: "Model Validation and Evaluation Practices"
tags:
  - validation
  - calibration
  - performance-metrics
  - benchmarking
---

# Model Validation and Evaluation Practices

## Purpose

Model validation determines whether a model is a sufficiently accurate representation of the real system for its intended purpose. This document establishes the community's expectations for how models are calibrated, evaluated, and tested before their outputs are used in research publications or applied decision-making.

## Scope

Applies to process-based and data-driven models used in soil, hydrological, geophysical, geomorphological, and climate research.

## Requirements

- [ ] Split available observational data into independent **calibration** and **validation** (withheld) periods or spatial extents before any model fitting.
- [ ] Report performance metrics on the **validation set only** as the primary evidence of model skill.
- [ ] Use at least two complementary performance metrics relevant to the application (e.g., KGE + percent bias for streamflow; RMSE + R² for regression outputs).
- [ ] Perform **temporal validation**: evaluate the model on a time period not used for calibration.
- [ ] Perform **spatial validation** (for distributed models): evaluate at gauging points or sites withheld from calibration.
- [ ] Document and justify the choice of objective function used for calibration.

## Recommended Practices

- Use k-fold cross-validation when the dataset is too small for a held-out validation set.
- Compare model performance against a **benchmark model** (e.g., climatological mean, persistence model, or simpler baseline) to demonstrate added value.
- Evaluate model performance across the full range of conditions (low flows, high flows, dry seasons, wet seasons) rather than only overall metrics.
- Conduct **process-based diagnostic evaluation**: check that modelled internal fluxes (e.g., soil moisture, evapotranspiration) are consistent with independent observations.
- Report performance metrics including their temporal variability (e.g., annual KGE distribution).

## Anti-Patterns to Avoid

- Evaluating a model on the same data used for calibration and calling it "validation".
- Over-fitting: achieving high calibration performance at the expense of structural realism.
- Using only R² as a performance metric, which does not penalise bias.
- Comparing modelled outputs to observations without accounting for observational uncertainty.
- Declaring a model "validated" without specifying the conditions and scales within which validation was performed.

## Tools & Resources

| Resource | Purpose |
|----------|---------|
| HydroGOF (R) | Goodness-of-fit metrics for hydrological models |
| hydroeval (Python) | Hydrological performance metrics |
| SPOTPY | Python model calibration and uncertainty analysis |
| ESMValTool | Systematic evaluation of climate model performance |
| scikit-learn | Cross-validation and regression metrics for ML models |

## References

- Moriasi et al. (2007) — Model evaluation guidelines for systematic quantification of accuracy in watershed simulations, Transactions of the ASABE
- Gupta et al. (2009) — Decomposition of the mean squared error and NSE: Implications for improving hydrological modelling, Journal of Hydrology
- Klemeš, V. (1986) — Operational testing of hydrological simulation models, Hydrological Sciences Journal
