# Hypocycloid Motion in the Melvin Magnetic Universe

A completed numerical reproduction and follow-up exploration project based on:

> Y.-K. Lim, *Hypocycloid motion in the Melvin magnetic universe*, arXiv:2004.08027 (2020).

## Overview

This project studies the motion of charged test particles in the Melvin magnetic universe.

The main goal is to reproduce the hypocycloid-like trajectories obtained in the weak-field regime and to test them using the full equations of motion rather than only the weak-field approximation.

The project also explores how these trajectories change as the magnetic field and other parameters vary.

## Physical Setting

The Melvin universe is an exact Einstein–Maxwell spacetime containing a magnetic field.

A charged particle in this spacetime is influenced by both the spacetime geometry and the electromagnetic field. Under special weak-field conditions, its trajectory can become very close to a standard hypocycloid.

As the field becomes stronger, the orbit deforms and can approach a narrow oscillation around a circular orbit.

## Reproduction Work

The completed reproduction includes:

- reconstruction of the full equations of motion for charged particles in the Melvin magnetic universe;
- numerical integration of the full equations;
- reproduction of hypocycloid-like trajectories in the weak-field regime;
- comparison between numerical trajectories and standard hypocycloids;
- geometric validation using normalized RMS and maximum deviations;
- generation of orbit plots and validation results.

The numerical tests support the weak-field result of the paper: when the cusp condition, the theoretical charge relation, and a sufficiently small weak-field control quantity are imposed together, the full equations produce trajectories that are very close to standard hypocycloids.

## Parameter Constraints

For hypocycloid-like candidates, the numerical construction uses:

\[
P=0,
\]

\[
r_+=r_*,
\]

\[
L=\frac{eBr_*^2}{2\Lambda_*},
\]

\[
E=\Lambda_*,
\]

and the weak-field charge relation

\[
e_n=\frac{n-2}{\sqrt{2(n-1)}}.
\]

The weak-field control quantity is

\[
e^2B^2.
\]

These conditions are used together because a hypocycloid-like orbit is not produced by arbitrary independent choices of all parameters.

## Numerical Findings

A constrained parameter scan was used to test the full equations over multiple magnetic-field strengths, outer radii, and cusp numbers.

The validation showed that:

- the theoretical weak-field charge gives the best agreement with standard hypocycloids in the tested regime;
- small charge deviations can significantly worsen the geometric agreement;
- the full equations reproduce the expected weak-field behavior with small but nonzero finite-field corrections;
- the orbit family changes continuously as the magnetic field is varied.

The measured numerical deviations should be distinguished from the theoretical weak-field order estimate \(O(e^2B^2)\).

## Follow-Up Exploration

The project also studies a parameterized family of deformed closed trajectories.

For fixed cusp number `n` and outer cusp radius `r_*`, the magnetic field `B` can be treated as a control parameter. The charge can then be adjusted numerically to satisfy the closed-orbit condition

\[
\Delta\phi=\frac{2\pi}{n}.
\]

This defines a numerical continuous family

\[
B\longmapsto
\bigl(
e(B),L(B),E(B),r_-(B),\text{orbit}(B)
\bigr).
\]

This is a numerical continuation framework for deformed hypocycloid-like orbits. It is not claimed to be a closed-form analytic family of exact hypocycloids.

## Scope

This project is a completed numerical reproduction with a computational follow-up exploration.

The results show high-accuracy numerical agreement with standard hypocycloids in the weak-field regime. They do not claim that finite-magnetic-field trajectories are exact analytic hypocycloids.

## Reference

Y.-K. Lim, *Hypocycloid motion in the Melvin magnetic universe*, arXiv:2004.08027 (2020).
