# Numerical Validation of Hypocycloid-Like Orbits

## Aim

This stage tests whether the hypocycloid-like trajectories described in Lim's paper can be reproduced by numerically integrating the full charged-particle equations in the Melvin magnetic universe.

The calculation uses the full equations of motion, not only the weak-field approximation.

## Parameter Construction

For candidate hypocycloid-like orbits, the scan imposes the following conditions:

- Motion is restricted to a plane by taking `P = 0`.
- The selected outer radius is also the cusp position, `r_+ = r_*`.
- The cusp condition determines the angular momentum:

\[
L=\frac{eBr_*^2}{2\Lambda_*}.
\]

- The radial constraint at the cusp determines the energy:

\[
E=\Lambda_*.
\]

- The weak-field charge relation is used as the reference value:

\[
e_n=\frac{n-2}{\sqrt{2(n-1)}}.
\]

- Candidates are retained only when

\[
e^2B^2 \leq 10^{-5}.
\]

These constraints reduce the scan to physically relevant candidates instead of independently choosing every parameter.

## Numerical Method

The trajectories are integrated with the full Melvin equations using a high-accuracy numerical ODE solver.

Each numerical trajectory is converted to Cartesian coordinates and compared with a standard hypocycloid having the same cusp number and outer radius.

The measured geometric errors are:

\[
\mathrm{NRMS}=
\frac{\sqrt{N^{-1}\sum_i d_i^2}}{r_+},
\qquad
\mathrm{NMAX}=
\frac{\max_i d_i}{r_+},
\]

where \(d_i\) is the distance from a numerical trajectory point to the reference hypocycloid.

The selected acceptance thresholds are:

- `NRMS <= 1e-3`
- `NMAX <= 3e-3`

The scan also records closure error and the residual of the radial constraint.

## Scan Range

| Parameter | Values |
| --- | --- |
| Magnetic field `B` | 0.0005, 0.001, 0.002, 0.003 |
| Outer radius `r_*` | 4, 6, 8 |
| Cusp number `n` | 3, 4, 5, 6 |
| Charge | `e_n(1-0.02)`, `e_n`, `e_n(1+0.02)` |
| Longitudinal momentum `P` | 0 |

After applying the weak-field control condition, the scan contains 129 candidates.

## Results

- 42 of 129 constrained candidates passed the selected geometric thresholds.
- The accepted cases used the theoretical weak-field charge value `e = e_n`.
- In this scan, charge values shifted by plus or minus 2% did not pass the same strict geometric thresholds.
- The accepted cases have normalized RMS deviations from approximately `1.7e-5` to `5.3e-4`.
- The accepted cases have normalized maximum deviations below approximately `1.34e-3`.

A representative accepted case is:

```text
B = 0.0005
r_* = 4
n = 3
e = 0.5
L = 0.001999998
NRMS = 1.73e-5
NMAX = 4.18e-5
```

## Interpretation and Limitations

The results support the weak-field result of the paper: under the cusp condition, the theoretical charge relation, and sufficiently small `e^2B^2`, solutions of the full equations can be numerically very close to standard hypocycloids.

However, these results do not prove that finite-magnetic-field trajectories are exact analytic hypocycloids. The finite deviations are expected because the full equations contain higher-order corrections beyond the weak-field approximation.

The quantity `O(e^2B^2)` is a theoretical order estimate; it is not treated as a measured geometric error.

## Reproducibility

The scan script is located in `src/melvin_bruteforce_scan.py`.

The filtering script is located in `src/filter_hypocycloid_scan.py`.

The parameter sets that passed the selected thresholds are recorded in `data/scan_metrics_filtered.csv`.

## Reference

Y.-K. Lim, *Hypocycloid motion in the Melvin magnetic universe*, arXiv:2004.08027 (2020).
