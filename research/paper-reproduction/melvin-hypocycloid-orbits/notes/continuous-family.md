# A Continuous Family of Deformed Hypocycloid-Like Orbits

## Question

The weak-field analysis gives standard hypocycloid motion in a particular limit. A natural follow-up question is whether these orbits can be followed continuously as the magnetic field changes.

This note defines a numerical continuation problem for such a family. It does not claim a closed-form analytic family of exact hypocycloids.

## Basic Construction

Fix:

- the cusp number $n$;
- the outer cusp radius $r_*$;
- the magnetic field $B$.

For a cusp at $r = r_*$, impose

```math
\dot r=0,
\qquad
\dot\phi=0.
```

These conditions determine the angular momentum and energy:

```math
L(B,e)=\frac{eBr_*^2}{2\Lambda_*},
\qquad
E(B)=\Lambda_*,
```

where

```math
\Lambda_*=1+\frac14B^2r_*^2.
```

After these constraints are imposed, the charge $e$ is the main remaining parameter.

## Closed-Orbit Condition

For an orbit with $n$ cusps, the angle between neighbouring outer cusps must be

```math
\Delta\phi=\frac{2\pi}{n}.
```

Define the closure residual

```math
F(B,e;n,r_*)=
\Delta\phi(B,e)-\frac{2\pi}{n}.
```

A continuous family of closed cusp orbits is then defined implicitly by

```math
F(B,e(B);n,r_*)=0.
```

For every selected value of $B$, a numerical root-finding method can adjust $e$ until the closure condition is satisfied.

The resulting family has the form

```math
B\longmapsto
\bigl(
e(B),L(B),E(B),r_-(B),\text{orbit}(B)
\bigr).
```

## Weak-Field Starting Point

At sufficiently small magnetic field, the natural initial charge is the weak-field value

```math
e_n=\frac{n-2}{\sqrt{2(n-1)}}.
```

The numerical validation project shows that this value produces trajectories close to standard hypocycloids when the weak-field control quantity $e^2 B^2$ is small.

This provides a practical starting point for numerical continuation.

## Numerical Continuation Procedure

For fixed $(n, r_*)$:

1. Choose a small initial field $B_0$.
2. Start from $e(B_0) \approx e_n$.
3. Numerically solve $F(B_0, e) = 0$.
4. Increase the field by a small step.
5. Use the previous solution as the initial guess for the next value of $e$.
6. Repeat while recording $e(B)$, $L(B)$, $E(B)$, the inner turning point $r_-(B)$, closure error, and constraint residual.

A useful set of outputs is:

- $e(B)$;
- $L(B)$ and $E(B)$;
- $r_-(B)$;
- the radial width $(r_* - r_-)/r_*$;
- the closure residual;
- representative trajectory plots.

## Interpretation

Near the weak-field end, the orbit is close to a standard hypocycloid.

As the magnetic field changes, the orbit may become a continuously deformed hypocycloid-like closed trajectory. In a narrow-radial-range regime, it may approach a small oscillation around a circular orbit.

This is a numerical research direction rather than an analytic proof. The term “continuous family” means a parameterized branch of numerical closed-orbit solutions.

## Scope and Limitations

- No closed-form expression for the full family is claimed.
- No claim is made that finite-field trajectories are exact standard hypocycloids.
- A root may fail to exist, become non-unique, or form a turning point as $B$ changes.
- Any proposed branch should be checked using closure and constraint-residual diagnostics.

## Reference

Y.-K. Lim, *Hypocycloid motion in the Melvin magnetic universe*, arXiv:2004.08027 (2020).
