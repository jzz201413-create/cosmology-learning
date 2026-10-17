#!/usr/bin/env python3
"""Brute-force verification of hypocycloid-like charged-particle orbits in Melvin spacetime.

Implements the *full*, non-perturbative equations (5) and (8) of
Y.-K. Lim, arXiv:2004.08027, not the weak-field expansion (27)-(29).

Two scan modes are provided.
  cusp (default): the paper's r_+ = r_* construction.  Choose (B, r_*, n)
      and set e=(n-2)/sqrt(2(n-1)), L=e*B*r_*^2/(2 Lambda_*).
  free-apocentre: a genuine grid over (B, e, L, r_+, n).  It starts at the
      chosen outer turning point r_+ with rdot=0 and computes E from Eq. (6).
      It does not assume the weak-field charge relation or r_+=r_*.

Requirements: numpy, pandas, scipy.  Example:
  python melvin_bruteforce_scan.py --figure3 --out results
  python melvin_bruteforce_scan.py --mode free-apocentre --B .001,.003,.01 --r-star 4,6,8 --e .25,.5,1 --L .002,.005,.01,.02 --n 3,4,5 --out results
  python melvin_bruteforce_scan.py --hypocycloid-grid --B .0005,.001,.002,.003 --r-star 4,6,8 --n 3,4,5,6 --e-relative-offsets -.02,0,.02 --out results
"""
from __future__ import annotations

import argparse
import json
from functools import partial
from dataclasses import asdict, dataclass
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.integrate import solve_ivp
from scipy.spatial import cKDTree


@dataclass(frozen=True)
class Case:
    B: float
    r_star: float
    n: int
    P: float = 0.0
    e: float | None = None
    L: float | None = None
    mode: str = "cusp"


def lam(r: np.ndarray | float, B: float) -> np.ndarray | float:
    return 1.0 + 0.25 * B * B * np.asarray(r) ** 2


def lam_prime(r: np.ndarray | float, B: float) -> np.ndarray | float:
    return 0.5 * B * B * np.asarray(r)


def weak_field_charge(n: int) -> float:
    """Equation (32), valid for integer n >= 3 in this polar-coordinate solver."""
    if n < 3:
        raise ValueError(
            "n=2 is the radial straight-line limit; it crosses r=0 and is not handled here.")
    return (n - 2.0) / np.sqrt(2.0 * (n - 1.0))


def cusp_constants(case: Case) -> tuple[float, float, float]:
    """Return physical (e, L, E), imposing either the cusp or free-apocentre setup."""
    if case.mode == "cusp":
        e = weak_field_charge(case.n) if case.e is None else case.e
        ls = float(lam(case.r_star, case.B))
        # Equation (12) inverted: L = e B r_*^2 / (2 Lambda_*).
        L = e * case.B * case.r_star**2 / \
            (2.0 * ls) if case.L is None else case.L
        # At the cusp K=0, Eq. (6) gives E^2-P^2=Lambda_*^2.
        E = np.sqrt(case.P**2 + ls**2)
        return e, L, E
    if case.mode != "free-apocentre" or case.e is None or case.L is None:
        raise ValueError("free-apocentre mode requires explicit e and L")
    e, L = case.e, case.L
    ls = float(lam(case.r_star, case.B))
    K = L - e * case.B * case.r_star**2 / (2.0 * ls)
    # Eq. (6) at the selected apocentre, where rdot=0.
    E = np.sqrt(case.P**2 + ls**4 * K**2 / case.r_star**2 + ls**2)
    return e, L, E


def rhs(tau: float, y: np.ndarray, *, B: float, e: float, L: float, E: float, P: float) -> np.ndarray:
    """Full equations: rdot=v, rddot=Eq.(8), phidot/tdot/zdot=Eq.(5)."""
    r, v, phi, tcoord, z = y
    if r <= 0.0:
        raise FloatingPointError(
            "r reached zero; polar equations are singular there.")
    la = float(lam(r, B))
    lp = float(lam_prime(r, B))
    K = L - e * B * r * r / (2.0 * la)
    rdd = (
        -(lp / la) * v * v
        + (P * P - E * E) * lp / la**5
        + (1.0 / r**3) * (1.0 - r * lp / la) * K * K
        + (e * B * la / r) * (1.0 - r * lp / (2.0 * la)) * K
    )
    return np.array([v, rdd, la**2 * K / r**2, E / la**2, P / la**2])


def invariant_residual(r: np.ndarray, v: np.ndarray, *, B: float, e: float, L: float, E: float, P: float) -> np.ndarray:
    """Eq. (6) residual: Lambda^4 rdot^2 - (E^2-P^2-V_eff^2)."""
    la = lam(r, B)
    K = L - e * B * r**2 / (2.0 * la)
    veff2 = la**4 * K**2 / r**2 + la**2
    return la**4 * v**2 - (E**2 - P**2 - veff2)


def standard_hypocycloid(n: int, r_plus: float, points: int = 100_000) -> np.ndarray:
    """Appendix A, Eq. (35), aligned so a cusp is at (r_plus, 0)."""
    b = r_plus / n
    u = np.linspace(0.0, 2.0 * np.pi, points, endpoint=False)
    return np.column_stack((
        b * ((n - 1.0) * np.cos(u) + np.cos((n - 1.0) * u)),
        b * ((n - 1.0) * np.sin(u) - np.sin((n - 1.0) * u)),
    ))


def integrate_case(case: Case, samples: int, rtol: float, atol: float) -> tuple[pd.DataFrame, dict]:
    e, L, E = cusp_constants(case)
    initial_acceleration = rhs(0.0, np.array([case.r_star, 0.0, 0.0, 0.0, 0.0]),
                               B=case.B, e=e, L=L, E=E, P=case.P)[1]
    if initial_acceleration >= 0.0:
        raise ValueError(
            "selected r_star is not an outer turning point (initial rddot >= 0)")
    scale = max(abs(e * case.B), 1.0e-6)
    # This is an integration bound, not a physics approximation.  It is deliberately
    # generous; success additionally requires n returns to an outer radial turning point.
    tau_max = 200.0 * case.r_star / scale
    max_step = 0.05 * case.r_star / scale

    def outer_turn(tau: float, y: np.ndarray) -> float:
        # At an outer turning point rdot changes from positive to negative.  Do not
        # use r-r_star here: tiny energy errors make the returned apocentre differ
        # from r_star by roundoff even when the radial cycle is correctly resolved.
        return y[1]
    outer_turn.direction = -1.0
    # solve_ivp accepts a positive integer here: stop after that many events.
    # The first event is the initial apocentre, so n+1 means n completed returns.
    outer_turn.terminal = case.n + 1

    y0 = np.array([case.r_star, 0.0, 0.0, 0.0, 0.0])
    ode = partial(rhs, B=case.B, e=e, L=L, E=E, P=case.P)
    sol0 = solve_ivp(
        ode, (0.0, tau_max), y0,
        events=outer_turn, method="DOP853", rtol=rtol, atol=atol, max_step=max_step,
    )
    events = sol0.t_events[0]
    # The initial state is an event; discard it and retain later apocentres.
    events = events[events > max(1e-12, tau_max * 1e-14)]
    if len(events) < case.n:
        raise RuntimeError(
            f"only {len(events)} outer turning points before tau_max={tau_max:g}; needed {case.n}")
    tau_end = float(events[case.n - 1])
    tau = np.linspace(0.0, tau_end, samples)
    sol = solve_ivp(
        ode, (0.0, tau_end), y0, t_eval=tau,
        method="DOP853", rtol=rtol, atol=atol, max_step=max_step,
    )
    if not sol.success:
        raise RuntimeError(sol.message)
    r, v, phi, tcoord, z = sol.y
    x, y = r * np.cos(phi), r * np.sin(phi)
    residual = invariant_residual(r, v, B=case.B, e=e, L=L, E=E, P=case.P)
    traj = pd.DataFrame({"tau": tau, "r": r, "rdot": v, "phi": phi, "t": tcoord, "z": z,
                         "x": x, "y": y, "constraint_residual": residual})

    tree = cKDTree(standard_hypocycloid(case.n, case.r_star))
    distance, _ = tree.query(np.column_stack((x, y)), k=1)
    metrics = {
        **asdict(case), "e": e, "L": L, "E": E,
        "r_minus_measured": float(np.min(r)), "r_plus_target": case.r_star,
        "initial_rddot": float(initial_acceleration),
        "tau_end": tau_end, "phi_end": float(phi[-1]),
        "closure_distance_over_rplus": float(np.hypot(x[-1] - case.r_star, y[-1]) / case.r_star),
        "rms_geometric_deviation": float(np.sqrt(np.mean(distance**2))),
        "max_geometric_deviation": float(np.max(distance)),
        "normalized_rms_geometric_deviation": float(np.sqrt(np.mean(distance**2)) / case.r_star),
        "normalized_max_geometric_deviation": float(np.max(distance) / case.r_star),
        "max_abs_constraint_residual": float(np.max(np.abs(residual))),
        # This is only the order estimate stated below Fig. 3, never a measured distance.
        "theory_O_e2B2": float(e * e * case.B * case.B),
        "equations": "full Eq.(5)+Eq.(8); metrics compared with Appendix-A Eq.(35)",
    }
    return traj, metrics


def parse_numbers(text: str, kind):
    return [kind(part.strip()) for part in text.split(",") if part.strip()]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--B", default="0.001",
                    help="comma-separated magnetic flux strengths")
    ap.add_argument("--mode", choices=("cusp",
                    "free-apocentre"), default="cusp")
    ap.add_argument("--r-star", default="6",
                    help="comma-separated chosen outer radii")
    ap.add_argument("--n", default="3,4,5",
                    help="comma-separated cusp counts (integers >=3)")
    ap.add_argument("--P", default="0",
                    help="comma-separated conserved z-momenta; Fig. 3 uses 0")
    ap.add_argument("--e", default="",
                    help="comma-separated charges; required by free-apocentre mode")
    ap.add_argument("--L", default="",
                    help="comma-separated angular momenta; required by free-apocentre mode")
    ap.add_argument("--hypocycloid-grid", action="store_true",
                    help="efficient constrained grid: enforce P=0, r_+=r_*, and derive L,E")
    ap.add_argument("--e-relative-offsets", default="0",
                    help="for --hypocycloid-grid, scan e=e_n*(1+offset); e_n is Eq.(32)")
    ap.add_argument("--weak-order-cap", type=float, default=1e-5,
                    help="for --hypocycloid-grid, reject candidates with e^2 B^2 above this value")
    ap.add_argument("--samples", type=int, default=12000)
    ap.add_argument("--rtol", type=float, default=1e-10)
    ap.add_argument("--atol", type=float, default=1e-12)
    ap.add_argument("--out", type=Path, default=Path("melvin_scan"))
    ap.add_argument("--figure3", action="store_true",
                    help="exact Figure-3 preset: B=.001, r_*=6, P=0, n=3,4,5")
    args = ap.parse_args()
    Bs = [0.001] if args.figure3 else parse_numbers(args.B, float)
    ns = [3, 4, 5] if args.figure3 else parse_numbers(args.n, int)
    rstars = [6.0] if args.figure3 else parse_numbers(args.r_star, float)
    Ps = [0.0] if args.figure3 else parse_numbers(args.P, float)
    es = parse_numbers(args.e, float) if args.e else [None]
    Ls = parse_numbers(args.L, float) if args.L else [None]
    offsets = parse_numbers(args.e_relative_offsets, float)
    if args.figure3:
        args.mode = "cusp"
    if args.mode == "free-apocentre" and (es == [None] or Ls == [None]):
        ap.error("--mode free-apocentre requires both --e and --L")
    if args.hypocycloid_grid and args.mode == "free-apocentre":
        ap.error("--hypocycloid-grid and --mode free-apocentre cannot be combined")
    if args.weak_order_cap <= 0.0:
        ap.error("--weak-order-cap must be positive")
    args.out.mkdir(parents=True, exist_ok=True)
    (args.out / "trajectories").mkdir(exist_ok=True)
    rows = []
    if args.hypocycloid_grid:
        # Necessary conditions for a sharp cusp in the paper's family:
        # P=0 (boost choice), r_+=r_*, and L,E fixed by Eqs. (12),(24).
        # Only B, r_*, n, and a controlled deviation from Eq.(32) remain to scan.
        cases = [
            Case(B=B, r_star=rstar, n=n, P=0.0,
                 e=weak_field_charge(n) * (1.0 + offset), mode="cusp")
            for B in Bs for rstar in rstars for n in ns for offset in offsets
            if weak_field_charge(n) * (1.0 + offset) > 0.0
            and (weak_field_charge(n) * (1.0 + offset) * B) ** 2 <= args.weak_order_cap
        ]
    else:
        cases = [
            Case(B=B, r_star=rstar, n=n, P=P, e=e, L=L, mode=args.mode)
            for B in Bs for rstar in rstars for n in ns for P in Ps for e in es for L in Ls
        ]
    if not cases:
        ap.error("no candidates remain after applying the requested constraints")
    total = len(cases)
    for case in cases:
        tag = (f"B{case.B:.8g}_r{case.r_star:.8g}_n{case.n}_P{case.P:.8g}"
               f"_e{case.e}_L{case.L}").replace(".", "p")
        try:
            traj, metrics = integrate_case(
                case, args.samples, args.rtol, args.atol)
            traj.to_csv(args.out / "trajectories" /
                        f"trajectory_{tag}.csv", index=False)
            metrics["status"] = "ok"
            metrics["message"] = ""
        except Exception as exc:  # retain failed parameter combinations in scan results
            metrics = {**asdict(case), "status": "failed", "message": str(exc)}
        rows.append(metrics)
        # Save after every case, so an interrupted long scan still has usable results.
        pd.DataFrame(rows).to_csv(args.out / "scan_metrics.csv", index=False)
        print(f"[{len(rows)}/{total}] " +
              json.dumps(metrics, ensure_ascii=False, default=float))
    pd.DataFrame(rows).to_csv(args.out / "scan_metrics.csv", index=False)


if __name__ == "__main__":
    main()
