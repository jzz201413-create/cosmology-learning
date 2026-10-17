# Energies and Angular Momenta of Periodic Schwarzschild Geodesics

A completed reproduction and computational extension project based on:

> J. Levin and G. Perez-Giz, *Energies and angular momenta of periodic Schwarzschild geodesics*, Physical Review D 77, 103005 (2008).

## Overview

This project reproduces the periodic-orbit framework for timelike Schwarzschild geodesics and studies its representation in angular-momentum–energy $(L, E)$ parameter space.

After reproducing the central orbital structure and generating the relevant figures, the project was extended through a broader brute-force numerical scan. The scan explores a wider range of parameters than the representative cases used in the initial reproduction.

## Periodic-Orbit Classification

Periodic bound orbits are described by the rational quantity

```math
q=w+\frac{v}{z},
```

or equivalently by the integer triplet $(z, w, v)$ together with orbital eccentricity.

- $z$ is the number of leaves in the orbit;
- $w$ is the number of additional near-circular whirls;
- $v$ is the step size between successive leaves.

These labels distinguish different zoom–whirl orbit structures and provide a systematic way to organize periodic geodesics.

## Reproduction Work

The completed reproduction includes:

- reconstruction of the periodic-orbit classification;
- study of the relation between $(z, w, v)$, eccentricity, and the rational parameter $q$;
- calculation of the conserved energy $E$ and angular momentum $L$ for periodic-orbit families;
- reproduction of the structure of periodic orbits in $(L, E)$ parameter space;
- generation of trajectory and parameter-space figures for visual validation.

The reproduction confirms the central qualitative result that periodic-orbit families organize into characteristic structures in the $(L, E)$ plane.

## Computational Extension

The project was extended beyond the initial representative examples through a brute-force parameter scan.

This broader exploration was used to:

- sample a wider region of the allowed parameter space;
- identify additional periodic-orbit candidates;
- examine how orbit structure changes with the conserved quantities;
- compare numerical trajectories across different orbit labels and parameter choices;
- expand the visual and numerical picture beyond the original set of reproduced examples.

The scan is an exploratory computational extension of the reproduction. It is intended to map and test the orbital parameter space, rather than to claim a new analytic classification.

## Project Contents

Suggested repository layout:

```text
schwarzschild-periodic-orbits-le/
  README.md
  figures/
  src/
  data/
  notes/
```

- `figures/` contains reproduced orbit and $(L, E)$ parameter-space plots.
- `src/` contains the numerical reproduction and brute-force scan code.
- `data/` contains scan outputs or selected candidate data.
- `notes/` contains derivations, parameter conventions, and validation notes.

## Scope

This project documents a completed computational reproduction together with a numerical extension of the explored parameter range.

The follow-up scan is evidence-based numerical exploration. It should be distinguished from a claim of a new closed-form analytic result.

## Related Projects

- `../periodic-orbits-fjwn/` — periodic orbits in the Fisher/Janis–Newman–Winicour spacetime.
- `../melvin-hypocycloid-orbits/` — charged-particle hypocycloid-like motion in the Melvin magnetic universe.

## Reference

J. Levin and G. Perez-Giz, *Energies and angular momenta of periodic Schwarzschild geodesics*, Physical Review D 77, 103005 (2008).
