---
id: culture-open-science-reproducibility
category: "open-science"
title: "Reproducibility Constraints in Geoscientific Research"
tags:
  - reproducibility
  - replicability
  - workflow
  - version-control
---

# Reproducibility Constraints in Geoscientific Research

## Purpose

Reproducibility — the ability to obtain the same results from the same data and methods — is a foundational scientific norm and an explicit cultural constraint for this research community. Field and laboratory data collection is often unrepeatable, making it essential that computational analyses and model outputs are fully reproducible from archived inputs.

## Principles

1. **Scripted analysis**: every data-processing step must be implemented in code, not through manual GUI operations that leave no audit trail.
2. **Version everything**: data, code, and configuration files must be under version control with meaningful commit messages.
3. **Self-contained environments**: analysis environments must be fully specified so that results can be reproduced on a different machine.
4. **Test before you trust**: automated tests must validate data-processing logic; failed tests block merges to main branches.
5. **Archive before you publish**: all inputs required to reproduce published results must be archived at the time of publication.

## Requirements

- [ ] All analysis workflows must be scripted (Python, R, Julia, Bash) and runnable end-to-end with a single command.
- [ ] Code repositories must include an environment specification file (`environment.yml`, `requirements.txt`, `renv.lock`, or equivalent).
- [ ] Workflows involving random processes must set and document random seeds.
- [ ] Model configuration files and parameter sets must be archived alongside model outputs.
- [ ] A DOI-linked code release must accompany every manuscript that includes computational analyses.

## Recommended Practices

- Use workflow managers (Snakemake, Nextflow, DVC pipelines) to formalise the analysis DAG and enable partial re-runs.
- Containerise the full software environment (Docker, Apptainer) for long-term reproducibility beyond dependency support lifetimes.
- Include a `notebooks/` directory for exploratory work but ensure final results come from scripted pipelines, not notebooks with hidden state.
- Add a `REPRODUCE.md` or equivalent that lists exact commands to reproduce every figure and table in the paper.

## Anti-Patterns to Avoid

- Editing data files manually without recording the change in code or a change log.
- Hard-coding absolute file paths; use relative paths and configuration files instead.
- Publishing results from notebooks where cells were run out of order.
- Relying on system-installed software without version pinning.
- Storing large binary files in Git without Git LFS or an external store (DVC, S3).

## Tools & Resources

| Resource | Purpose |
|----------|---------|
| Git / GitHub | Version control for code and configuration |
| DVC | Data version control and pipeline management |
| Snakemake / Nextflow | Scientific workflow management |
| Docker / Apptainer | Software environment containerisation |
| Binder / Code Ocean | On-demand reproducible notebook environments |
| pytest / testthat | Unit and integration testing |

## References

- Baker, M. (2016) — 1,500 scientists lift the lid on reproducibility, Nature
- The Turing Way Community (2022) — The Turing Way: A Handbook for Reproducible, Ethical and Collaborative Research
- Sandve et al. (2013) — Ten Simple Rules for Reproducible Computational Research, PLOS Computational Biology
