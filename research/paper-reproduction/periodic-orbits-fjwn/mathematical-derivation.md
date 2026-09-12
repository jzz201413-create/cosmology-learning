# Mathematical Derivation

This document reorganizes the mathematical reconstruction developed from
the paper *Periodic orbits around a spherically symmetric naked
singularity*. The purpose is to record the main derivational chain rather
than reproduce the paper word-for-word.

## 1. F/JNW Metric

The F/JNW metric used in the paper is

```math
ds^2 =
-f^\nu dt^2
+f^{-\nu}dr^2
+r^2f^{1-\nu}
\left(d\theta^2+\sin^2\theta\,d\phi^2\right),
```

with

```math
f=1-\frac{r_g}{r}.
```

The metric is taken as the known F/JNW solution; its derivation from the
Einstein-scalar field equations is outside the scope of this reproduction.

> **Notation note:** The source notes contain one occurrence where the
> scalar-field parameter is labelled $V$, while the equations consistently
> use $\nu$. The derivation here uses $\nu$ consistently.

---

## 2. Geodesic Lagrangian and Conjugate Momenta

For geodesic motion, use the Lagrangian

```math
L=\frac12 g_{\mu\nu}\dot{x}^{\mu}\dot{x}^{\nu}.
```

Substituting the F/JNW metric gives

```math
L=
\frac12
\left[
-f^\nu\dot t^2
+f^{-\nu}\dot r^2
+r^2f^{1-\nu}
\left(
\dot\theta^2+\sin^2\theta\,\dot\phi^2
\right)
\right].
```

Define the conjugate momentum by

```math
p_\mu=\frac{\partial L}{\partial\dot{x}^{\mu}}.
```

The four non-zero conjugate momenta are

```math
p_t=-f^\nu\dot t,
```

```math
p_r=f^{-\nu}\dot r,
```

```math
p_\theta=r^2f^{1-\nu}\dot\theta,
```

```math
p_\phi=r^2f^{1-\nu}\sin^2\theta\,\dot\phi.
```

These correspond to Eq. (4) of the paper.

---

## 3. Hamiltonian

The Hamiltonian is obtained from the Legendre transformation

```math
H=p_\mu\dot{x}^{\mu}-L.
```

Using

```math
p_\mu=g_{\mu\nu}\dot{x}^{\nu},
\qquad
\dot{x}^{\mu}=g^{\mu\nu}p_\nu,
```

the Hamiltonian can be written as

```math
H=\frac12 g^{\mu\nu}p_\mu p_\nu.
```

Since the metric is diagonal, its inverse has the non-zero components

```math
g^{tt}=-f^{-\nu},
\qquad
g^{rr}=f^\nu,
```

```math
g^{\theta\theta}=
\frac{1}{r^2f^{1-\nu}},
\qquad
g^{\phi\phi}=
\frac{1}{r^2f^{1-\nu}\sin^2\theta}.
```

Therefore,

```math
H=
\frac12
\left[
-f^{-\nu}p_t^2
+f^\nu p_r^2
+\frac{p_\theta^2}{r^2f^{1-\nu}}
+\frac{p_\phi^2}{r^2f^{1-\nu}\sin^2\theta}
\right].
```

This is Eq. (5).

---

## 4. Conserved Energy and Angular Momentum

Hamilton's equations give

```math
\dot p_\mu=-\frac{\partial H}{\partial x^\mu}.
```

The Hamiltonian contains neither $t$ nor $\phi$ explicitly, so

```math
\frac{\partial H}{\partial t}=0,
\qquad
\frac{\partial H}{\partial\phi}=0.
```

Hence

```math
\dot p_t=0,
\qquad
\dot p_\phi=0.
```

Both momenta are conserved.

Define

```math
p_t=-E,
\qquad
p_\phi=L,
```

where $E$ is the conserved energy and $L$ is the conserved angular
momentum.

Using the expressions for the conjugate momenta,

```math
-E=-f^\nu\dot t,
```

and

```math
L=r^2f^{1-\nu}\sin^2\theta\,\dot\phi.
```

Therefore,

```math
\dot t=f^{-\nu}E,
```

and

```math
\dot\phi=
\frac{L}{r^2f^{1-\nu}\sin^2\theta}.
```

These correspond to Eqs. (6) and (7).

---

## 5. Hamilton Equations for $r$ and $\theta$

For the remaining coordinates,

```math
\dot r=\frac{\partial H}{\partial p_r},
\qquad
\dot p_r=-\frac{\partial H}{\partial r},
```

and

```math
\dot\theta=\frac{\partial H}{\partial p_\theta},
\qquad
\dot p_\theta=-\frac{\partial H}{\partial\theta}.
```

The coordinate equations obtained from the Hamiltonian are

```math
\dot r=f^\nu p_r,
```

and

```math
\dot\theta=
\frac{p_\theta}{r^2f^{1-\nu}}.
```

The corresponding momentum equations follow by differentiating the
Hamiltonian with respect to $r$ and $\theta$. These are the equations
given as Eqs. (8)--(11) in the paper.

---

## 6. Separation of Radial and Angular Motion

For timelike particles, the Hamiltonian constraint is

```math
H=-\frac12.
```

or equivalently,

```math
2H=-1.
```

Substituting

```math
p_t=-E,
\qquad
p_\phi=L
```

into the Hamiltonian gives

```math
-f^{-\nu}E^2
+f^\nu p_r^2
+\frac{p_\theta^2}{r^2f^{1-\nu}}
+\frac{L^2}{r^2f^{1-\nu}\sin^2\theta}
=-1.
```

Multiplying by $f^\nu$ and separating the angular dependence leads to
a separation constant. The angular part can be written as

```math
K=
p_\theta^2+
\frac{L^2\cos^2\theta}{\sin^2\theta}.
```

For the radial motion, the resulting expression is

```math
f^{2\nu}p_r^2
=
E^2
-f^\nu
\left(
1+\frac{L^2}{r^2f^{1-\nu}}
\right)
-\frac{Kf^{2\nu-1}}{r^2}.
```

The radial and angular motions are therefore separated.

---

## 7. Effective Potential

For the orbital analysis, the motion can be restricted to the equatorial
plane,

```math
\theta=\frac{\pi}{2},
\qquad
p_\theta=0.
```

Then the radial equation becomes

```math
\dot r^2
=
E^2
-\frac{L^2}{r^2}f^{2\nu-1}
-f^\nu.
```

Define the effective potential through

```math
V_{\mathrm{eff}}^2(r)
=
\frac{L^2}{r^2}f^{2\nu-1}
+f^\nu.
```

The radial equation is then

```math
\dot r^2
=
E^2-V_{\mathrm{eff}}^2(r).
```

This is the effective-potential form corresponding to Eq. (14).

At a radial turning point,

```math
\dot r=0,
```

so

```math
E^2=V_{\mathrm{eff}}^2(r).
```

---

## 8. Circular Orbits

A circular orbit has constant radial coordinate. Therefore,

```math
\dot r=0,
\qquad
\frac{dV_{\mathrm{eff}}^2}{dr}=0.
```

Starting from

```math
V_{\mathrm{eff}}^2
=
\frac{L^2}{r^2}f^{2\nu-1}
+f^\nu,
```

the circular-orbit condition gives

```math
L^2
=
\frac{\nu r^2r_g f^{1-\nu}}
{2r-(1+2\nu)r_g}.
```

Taking the positive root,

```math
L=
r
\sqrt{
\frac{\nu r_g f^{1-\nu}}
{2r-(1+2\nu)r_g}
}.
```

Using the circular-orbit condition in the effective potential gives

```math
E=
f^{\nu/2}
\sqrt{
\frac{2r-(1+\nu)r_g}
{2r-(1+2\nu)r_g}
}.
```

These expressions correspond to Eq. (15).

---

## 9. Critical Radius for Circular Orbits

The denominator in the circular-orbit expressions requires

```math
2r-(1+2\nu)r_g>0.
```

The corresponding critical radius is

```math
r=
\frac12(1+2\nu)r_g.
```

This is Eq. (16).

---

## 10. Marginally Stable Circular Orbits

A circular orbit satisfies

```math
\frac{dV_{\mathrm{eff}}^2}{dr}=0.
```

The marginally stable case additionally satisfies

```math
\frac{d^2V_{\mathrm{eff}}^2}{dr^2}=0.
```

Substituting the circular-orbit expression for $L^2$ into the second
derivative condition produces the quadratic equation

```math
r^2
-r_g(1+\nu)r
+\frac12r_g^2(1+\nu)(1+2\nu)
=0.
```

Solving this equation gives the possible critical radii listed in
Eq. (17) of the paper.

The corresponding angular momentum and energy are obtained by substituting
the critical radius into the circular-orbit expressions. These relations
are summarized in Eq. (18).

---

## 11. Average Angular Momentum

For a given value of $\nu$, the paper considers the angular momenta
associated with marginally bound and marginally stable circular orbits.

Denoting them by $L_{\mathrm{mb}}$ and $L_{\mathrm{ms}}$, the paper
defines a representative angular momentum through their average,

```math
L=\frac12
\left(
L_{\mathrm{mb}}+L_{\mathrm{ms}}
\right).
```

This provides the angular-momentum choice used in the subsequent analysis
of periodic orbits.

---

## 12. Periodic Orbits

Let $r_+$ denote the apastron and $r_-$ the periastron.

At a turning point,

```math
\dot r=0,
```

so the radial equation gives

```math
E^2=V_{\mathrm{eff}}^2(r).
```

The angular displacement during one complete radial oscillation can be
obtained from

```math
\frac{d\phi}{dr}
=
\frac{\dot\phi}{\dot r}.
```

Therefore,

```math
\Delta\phi
=
2\int_{r_-}^{r_+}
\frac{\dot\phi}{\dot r}\,dr.
```

Using

```math
\dot\phi=
\frac{L}{r^2f^{1-\nu}}
```

and

```math
\dot r=
\sqrt{
E^2-
\left(
\frac{L^2}{r^2}f^{2\nu-1}
+f^\nu
\right)
},
```

the angular advance becomes

```math
\Delta\phi
=
2\int_{r_-}^{r_+}
\frac{
L\,dr
}{
r^2f^{1-\nu}
\sqrt{
E^2-
\left(
\frac{L^2}{r^2}f^{2\nu-1}
+f^\nu
\right)
}
}.
```

The paper then introduces a dimensionless quantity $q$ to describe the
angular advance associated with one radial period.

---

## 13. Classification of Periodic Orbits

Periodic orbits occur when the relevant orbital frequency ratio is
rational.

The paper writes

```math
q=w+\frac{v}{z},
```

where $z$, $w$, and $v$ are integers.

They characterize different geometric aspects of the orbit:

- $z$: zoom number, describing the number of basic radial zooms;
- $w$: whirl number, describing the additional winding around the center;
- $v$: vertex number, describing the number of vertices formed by
  connecting successive apastra.

This provides a compact classification of the geometry of the periodic
orbits.

---

## 14. Reproduction Summary

The reconstructed mathematical chain is

```math
\boxed{
\text{F/JNW metric}
\rightarrow
\text{geodesic Lagrangian}
\rightarrow
\text{conjugate momenta}
\rightarrow
\text{Hamiltonian}
}
```

followed by

```math
\boxed{
\text{conserved }E,L
\rightarrow
\text{radial equation}
\rightarrow
V_{\mathrm{eff}}
\rightarrow
\text{circular orbits}
\rightarrow
\text{periodic orbits}
}
```

The main purpose of the reconstruction is to make the logical connection
between the equations explicit and to verify the mathematical structure
used in the paper.
