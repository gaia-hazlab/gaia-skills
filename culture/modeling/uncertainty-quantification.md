---
id: culture-modeling-uncertainty
category: "modeling"
title: "Uncertainty Quantification and Communication in Geoscientific Modelling"
tags:
  - uncertainty
  - sensitivity-analysis
  - ensemble
  - error-propagation
---

# Uncertainty Quantification and Communication in Geoscientific Modelling

## Purpose

All geoscientific models carry uncertainty arising from input data, parameter estimation, structural assumptions, and natural variability. This community requires that uncertainty be explicitly quantified, communicated, and considered in decision-making. Reporting a single "best estimate" without uncertainty bounds is considered insufficient scientific practice.

## Scope

Applies to all quantitative model outputs used in research publications, technical reports, or decision support within this community.

## Requirements

- [ ] Report uncertainty ranges (confidence intervals, credible intervals, or ensemble spread) alongside every key model output.
- [ ] Conduct and document a **sensitivity analysis** identifying the parameters to which model outputs are most sensitive.
- [ ] Where multiple model structures are plausible, use **multi-model ensembles** or model averaging rather than selecting a single model.
- [ ] Clearly distinguish between **aleatory uncertainty** (irreducible natural variability) and **epistemic uncertainty** (reducible knowledge gaps).
- [ ] Report the calibration and validation period performance metrics (e.g., NSE, KGE, RMSE, PBIAS) with uncertainty bounds.

## Recommended Practices

- Apply a formal uncertainty analysis framework:
  - **Monte Carlo methods**: for propagating input and parameter uncertainty.
  - **GLUE (Generalised Likelihood Uncertainty Estimation)**: Bayesian-compatible approach for equifinality in hydrological models.
  - **Bayesian inference (MCMC)**: for posterior parameter distributions when prior knowledge is available.
  - **Sobol / variance-based sensitivity analysis**: for ranking parameter importance.
- Visualise uncertainty with shaded ensemble envelopes, box plots, or probability density functions rather than only showing best-fit lines.
- Include a dedicated "Uncertainty and Limitations" section in all technical reports and papers.
- When communicating results to non-specialists, translate model uncertainty into probability statements or scenario ranges.

## Anti-Patterns to Avoid

- Reporting only the median or best-fit result without any indication of spread.
- Claiming model validation based on a single performance metric or a single calibration period.
- Conflating calibration performance with predictive skill in extrapolated conditions.
- Using deterministic sensitivity analysis (one-at-a-time perturbation) as the sole uncertainty method for non-linear models.
- Hiding poor model performance by choosing metrics that are insensitive to the type of errors present.

## Tools & Resources

| Resource | Purpose |
|----------|---------|
| SPOTPY | Python parameter estimation, calibration, and uncertainty analysis |
| SALib | Python sensitivity analysis library (Sobol, Morris, FAST) |
| emcee | Python MCMC ensemble sampler |
| PEST / BeoPEST | Parameter estimation and uncertainty analysis for external models |
| UQLab | MATLAB uncertainty quantification framework |
| arviz | Python/R Bayesian inference visualisation |

## References

- Beven, K. J. & Binley, A. M. (1992) — The future of distributed models: model calibration and uncertainty prediction, Hydrological Processes
- Saltelli et al. (2008) — Global Sensitivity Analysis: The Primer
- Walker et al. (2003) — Defining Uncertainty: A Conceptual Basis for Uncertainty Management in Model-Based Decision Support, Integrated Assessment
