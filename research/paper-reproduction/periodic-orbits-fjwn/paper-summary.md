# What Does This Paper Do?

> A concise summary of **“Periodic orbits around a spherically symmetric naked singularity”** based on the research notes developed from the paper.

## Research Motivation

The paper studies the motion of test particles around a naked singularity using the Fisher/Janis-Newman-Winicour (F/JNW) spacetime and compares the results with the Schwarzschild spacetime.

The F/JNW spacetime is associated with Einstein gravity coupled to a massless scalar field, whereas the Schwarzschild spacetime is a vacuum solution of Einstein's equations.

The additional scalar field changes the spacetime geometry and allows the solution to contain a naked singularity rather than a black-hole event horizon.

## F/JNW vs. Schwarzschild

| Spacetime | Physical setting |
| --- | --- |
| F/JNW | Einstein gravity + massless scalar field |
| Schwarzschild | Vacuum Einstein gravity |

The F/JNW spacetime is characterized by a mass parameter $r_g$ and a scalar-field parameter $\nu$.

## Research Question

The paper asks how timelike test particles move in the F/JNW spacetime, with particular attention to:

- geodesic motion;
- the effective potential;
- circular orbits;
- periodic orbits.

The analysis uses a Hamiltonian formulation of the geodesic equations.

## Method

The main mathematical route is:

```math
\text{F/JNW metric}
\rightarrow
\text{geodesic equations}
\rightarrow
\text{Hamiltonian formulation}
\rightarrow
\text{effective potential}
\rightarrow
\text{circular orbits}
\rightarrow
\text{periodic orbits}
```

The effective potential is used to analyze the radial motion of timelike test particles and to determine the conditions for circular orbits and their stability.

The paper also considers the innermost bound circular orbit (IBCO) and the innermost stable circular orbit (ISCO).

## Main Result 1: Potential Barrier

For

```math
\nu < \frac{1}{2},
```

particles with non-zero angular momentum encounter an infinite potential barrier as they approach the naked singularity.

In terms of the effective potential,

```math
V_{\mathrm{eff}} \rightarrow \infty
```

near the singularity at

```math
r=r_g.
```

Therefore, particles with non-zero angular momentum cannot reach the naked singularity.

The notes describe this result as being consistent with numerical results reported in earlier literature.

## Main Result 2: Periodic Orbits

The paper obtains periodic orbits in the F/JNW spacetime.

Periodic orbits are analyzed through the angular advance accumulated during radial motion. A dimensionless quantity $q$ is introduced to characterize the orbital structure, with the periodic-orbit condition expressed as

```math
q=w+\frac{v}{z},
```

where $z$, $w$, and $v$ characterize the zoom, whirl, and vertex structure of the orbit.

## Comparison with Schwarzschild

The paper compares periodic orbits in the F/JNW spacetime with corresponding periodic orbits around a Schwarzschild black hole.

The main qualitative result is that the same types of periodic orbits typically require lower energies in the F/JNW spacetime than in the Schwarzschild spacetime.

In symbolic form, the notes summarize this as

```math
E_{\mathrm{F/JNW}} < E_{\mathrm{Schwarzschild}}
```

for the same type of periodic orbit.

## What the Paper Actually Studies

The logical structure of the paper can be summarized as:

1. Specify the F/JNW spacetime.
2. Formulate timelike geodesic motion using the Hamiltonian.
3. Derive the effective potential.
4. Analyze circular orbits and their stability.
5. Determine the conditions for periodic orbits.
6. Compare the resulting orbital behavior with the Schwarzschild case.

The focus is therefore not simply on whether naked singularities exist, but on how their spacetime geometry affects the dynamics of test particles.

## Project Scope

This project is a **paper-reading and reproduction project**, not an independent research project.

The purpose is to reconstruct the mathematical framework of the paper, understand the physical meaning of its equations, and use computational tools to reproduce and check selected results.

Detailed derivations are documented separately in [`mathematical-derivation.md`](mathematical-derivation.md).

## Key Takeaway

The central physical point is that changing the spacetime geometry from Schwarzschild to F/JNW changes the structure of test-particle orbits.

In particular:

- for $\nu < 1/2$, non-zero angular momentum produces an infinite effective-potential barrier near the naked singularity;
- periodic orbits exist in the F/JNW spacetime;
- compared with Schwarzschild, the same periodic-orbit structures typically occur at lower energies in F/JNW.
