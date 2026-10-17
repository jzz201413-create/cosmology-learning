# Hypocycloid Motion in the Melvin Magnetic Universe

A completed numerical reproduction and follow-up exploration project based on:

> Y.-K. Lim, *Hypocycloid motion in the Melvin magnetic universe*, arXiv:2004.08027 (2020).

## Overview

This project studies charged-particle motion in the Melvin magnetic universe.

It reproduces the weak-field hypocycloid-like trajectories discussed in the paper and tests them by integrating the full, non-perturbative equations of motion. It also extends the reproduction through constrained numerical scans and an exploration of continuously deformed closed-orbit families.

## Physical Setting

The Melvin universe is an exact Einstein–Maxwell spacetime containing a magnetic field. A charged test particle is influenced by both the spacetime geometry and the electromagnetic field.

In the weak-field regime, special parameter choices produce trajectories that are very close to standard hypocycloids. As the field becomes stronger, these trajectories deform and can approach narrow oscillations around circular orbits.

## Reproduction Work

The completed reproduction includes:

- reconstruction and numerical integration of the full charged-particle equations;
- reproduction of weak-field hypocycloid-like trajectories;
- reproduction of the perturbed circular-orbit regime;
- comparison of numerical trajectories with standard hypocycloids;
- generation of trajectory and parameter-space figures;
- geometric validation using normalized RMS and maximum deviations.

## Constrained Numerical Scan

The scan uses the cusp construction with

\[
P=0,\qquad r_+=r_*,
\]

together with

\[
L=\frac{eBr_*^2}{2\Lambda_*},
\qquad
E=\Lambda_*,
\]

and the weak-field reference charge

\[
e_n=\frac{n-2}{\sqrt{2(n-1)}}.
\]

The scan retains candidates satisfying the weak-field control condition

\[
e^2B^2 \leq 10^{-5}.
\]

For the constrained scan:

- 129 parameter candidates were generated;
- 42 candidates passed the selected geometric thresholds;
- accepted cases used the theoretical weak-field charge value;
- small charge offsets did not pass the same strict thresholds in this scan.

These are high-accuracy numerical results, not a proof of exact analytic hypocycloid solutions at finite magnetic field.

## Follow-Up Exploration

The project also investigates a parameterized family of deformed closed trajectories.

For fixed cusp number `n` and outer cusp radius `r_*`, the magnetic field `B` is treated as a control parameter. The charge is adjusted numerically to satisfy

\[
\Delta\phi=\frac{2\pi}{n}.
\]

This defines a numerical family

\[
B\longmapsto
\bigl(e(B),L(B),E(B),r_-(B),\text{orbit}(B)\bigr).
\]

This is a numerical continuation framework, not a claimed closed-form analytic family of exact hypocycloids.

## Project Structure

- `figures/` — trajectory plots from the weak-field and perturbed-circular-orbit reproductions.
- `src/reproduce_melvin_limits.py` — reproduction of the two representative Melvin regimes.
- `src/melvin_bruteforce_scan.py` — full-equation constrained and free parameter scans.
- `src/filter_hypocycloid_scan.py` — filter for measured geometric-error thresholds.
- `data/scan_metrics_filtered.csv` — parameter sets passing the selected validation thresholds.
- `notes/validation-summary.md` — numerical validation method and results.
- `notes/continuous-family.md` — continuous-family formulation.
- `reports/` — selected concise PDF reproduction report.

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
