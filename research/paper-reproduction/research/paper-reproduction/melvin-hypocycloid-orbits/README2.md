# Hypocycloid Motion in the Melvin Magnetic Universe

A paper-reading, numerical-reproduction, and follow-up exploration project based on:

> Y.-K. Lim, *Hypocycloid motion in the Melvin magnetic universe*, arXiv:2004.08027 (2020).

## Overview

This project studies charged-particle trajectories in the Melvin magnetic universe. The main aim is to reproduce and numerically test the weak-field hypocycloid result described in the paper using the full equations of motion.

The project also develops a follow-up numerical framework for a continuous family of deformed hypocycloid-like closed orbits.

## Project Structure

- `notes/validation-summary.md` — Numerical validation method, parameter scan, measured errors, and limitations.
- `notes/continuous-family.md` — Definition of a parameterized continuous family of deformed closed orbits.
- `src/melvin_bruteforce_scan.py` — Full-equation numerical scan and trajectory generator.
- `src/filter_hypocycloid_scan.py` — Filter for measured geometric-error thresholds.
- `data/scan_metrics_filtered.csv` — Parameter sets that passed the selected numerical validation thresholds.
- `requirements.txt` — Python dependencies.

## Reproduction Status

The numerical scan uses the full non-perturbative Melvin equations rather than only the weak-field approximation.

For the constrained scan:

- 129 parameter candidates were generated after applying the weak-field control condition.
- 42 candidates passed the selected geometric thresholds.
- Accepted cases used the theoretical weak-field charge value.
- Small charge offsets did not pass the same strict thresholds in this scan.

These are numerical high-accuracy results. They should not be interpreted as a proof of exact analytic hypocycloid solutions at finite magnetic field.

## Scope

This is a paper-reading and reproduction project, with an exploratory numerical follow-up. It is not presented as an independent research publication or as a proof of new exact solutions.

The phrase “continuous family” refers here to a numerically defined parameterized family of closed orbits, not to a closed-form analytic family.

## Quick Start

```bash
pip install -r requirements.txt

python src/melvin_bruteforce_scan.py \
  --hypocycloid-grid \
  --B 0.0005,0.001,0.002,0.003 \
  --r-star 4,6,8 \
  --n 3,4,5,6 \
  --e-relative-offsets=-0.02,0,0.02 \
  --out results

python src/filter_hypocycloid_scan.py \
  results/scan_metrics.csv \
  --rms 1e-3 \
  --max 3e-3
```

## Reference

Y.-K. Lim, *Hypocycloid motion in the Melvin magnetic universe*, arXiv:2004.08027 (2020).
