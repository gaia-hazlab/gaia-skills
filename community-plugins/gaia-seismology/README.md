# gaia-seismology

Seismology workflows for GAIA HazLab. The first skill finds and corrects timing errors in seismic
phase picks; picks feed earthquake locations, catalogs and tomography, so a timing error at one
station biases all of them. It handles two failure modes: picks made on day-merged traces whose sample
count drifts away from the MiniSEED record-header times, and station clock errors where the
headers themselves are wrong. Clock corrections are applied only after a person confirms them.
Maintainer: @mdenolle.

## Skills

| Skill | What it does |
| --- | --- |
| `correcting-pick-timing` | Re-times picks from their own MiniSEED record headers (day-merge drift); screens every station for clock offsets, drifts and resets in network-relative travel-time residuals and cross-correlation differential times; writes a review report, models the confirmed clock errors and writes a new, corrected pick file with provenance |

## What it may run

The skill bundles the `pick_timing` Python package (version 0.1.0) in
`skills/correcting-pick-timing/scripts/`. It is a copy of `tools/pick_timing` at commit
`a8f6d5f164d09dfe4d74dd1251af35581cf79fe6` of
[Denolle-Lab/cascadia_obs_ensemble](https://github.com/Denolle-Lab/cascadia_obs_ensemble), MIT
licensed (see `skills/correcting-pick-timing/scripts/LICENSE`).

Requirements: Python 3.9 or later, numpy, scipy, pandas 2.0 or later, ObsPy 1.4 or later, PyYAML;
pyarrow only for Parquet tables; matplotlib (installed with ObsPy) for the HTML report. Tested with
Python 3.10, numpy 1.26.4, scipy 1.15.2, pandas 2.3.3, ObsPy 1.5.0 and PyYAML 6.0.3. The skill
tells the agent to check these are installed and to ask before installing anything.

Commands the skill tells the agent to run:

| Command | What it does | Network |
| --- | --- | --- |
| `python scripts/run_pick_timing.py <command> -c CONFIG.yaml` (or `python -m pick_timing ...` once installed) | Runs one of `scan-headers`, `retime`, `extract-nlloc`, `detect-clock`, `report`, `ingest-review`, `model-clock`, `apply`, `validate`, `relocate-nlloc`, `make-example` | Only `scan-headers` and `retime`, and only when the config's waveform reader is `fdsn` (or a `routed` reader with an `fdsn` route or fallback): they download MiniSEED with ObsPy from the FDSN data centre named in the config, such as EarthScope or NCEDC, about 1 to 10 MB per channel-day. The skill tells the agent to ask first and say how many station-days. Every other command reads local files only |
| `python -m unittest discover -s scripts/tests -t scripts` | The bundled unit tests (17 tests, about 15 s) | None |
| `pip install "pick-timing @ git+https://github.com/Denolle-Lab/cascadia_obs_ensemble@<commit>#subdirectory=tools/pick_timing"` | Optional: installs the same code, pinned to the commit above, into the user's environment. Only after the user agrees | GitHub, to fetch that commit |
| `md5sum <new pick file>` | Records the checksum of the corrected pick file | None |

What the code touches:

- **Reads** the pick, residual, station, origin and cross-correlation tables the user names in
  the config, and waveforms from the archive the config names (an SDS tree, an mseedindex
  SQLite index, opened read-only, or an FDSN data centre).
- **Writes** new files only, into the configured `output_dir` or the `--out` / `--output` path
  the user gives. `apply` writes a new pick file and never edits its input. `make-example`
  writes a small synthetic dataset into the folder given with `--out`.
- `relocate-nlloc` (optional validation) runs the NonLinLoc binary whose path the user passes
  with `--nlloc`, on copies of the run's control and observation files written into the output
  folder; the original run folder is only read.
- For provenance, the package runs `git rev-parse HEAD` and `git status --porcelain` on its own
  folder (read-only) and records the result in the `*.provenance.json` files.
- The HTML report is a single self-contained file: its figures are embedded as base64 PNG data
  URIs, and it loads nothing from the network.

The skill tells the agent to ask a person before downloading waveforms, writing outside the
project folder, overwriting any existing file, or applying a clock correction no person has
confirmed.

## Install

```bash
claude plugin marketplace add gaia-hazlab/gaia-skills
claude plugin install gaia-seismology@gaia-skills
```
