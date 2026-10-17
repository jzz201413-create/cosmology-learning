#!/usr/bin/env python3
"""Filter melvin_bruteforce_scan.py output by measured geometric errors.

Example:
  python filter_hypocycloid_scan.py melvin_scan/scan_metrics.csv --rms 1e-3 --max 3e-3

The theoretical column theory_O_e2B2 is deliberately not used as an error metric:
it is an order estimate from the weak-field derivation, whereas the two thresholds
below act on measured distances to the standard hypocycloid.
"""
from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd


REQUIRED = {"normalized_rms_geometric_deviation",
            "normalized_max_geometric_deviation"}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("input_csv", type=Path)
    ap.add_argument("--rms", type=float, required=True,
                    help="maximum normalized RMS geometric deviation")
    ap.add_argument("--max", dest="maxdev", type=float, required=True,
                    help="maximum normalized max geometric deviation")
    ap.add_argument("--closure", type=float, default=None,
                    help="optional max normalized closure distance")
    ap.add_argument("--constraint", type=float, default=None,
                    help="optional max Hamiltonian-constraint residual")
    ap.add_argument("--out", type=Path, default=None)
    args = ap.parse_args()
    if args.rms < 0 or args.maxdev < 0:
        ap.error("thresholds must be non-negative")
    df = pd.read_csv(args.input_csv)
    missing = REQUIRED - set(df.columns)
    if missing:
        raise ValueError(
            f"not a compatible scan CSV; missing {sorted(missing)}")
    accepted = df.copy()
    if "status" in accepted:
        accepted = accepted[accepted["status"].eq("ok")]
    accepted = accepted[
        accepted["normalized_rms_geometric_deviation"].le(args.rms)
        & accepted["normalized_max_geometric_deviation"].le(args.maxdev)
    ]
    if args.closure is not None:
        if "closure_distance_over_rplus" not in accepted:
            raise ValueError("CSV has no closure_distance_over_rplus column")
        accepted = accepted[accepted["closure_distance_over_rplus"].le(
            args.closure)]
    if args.constraint is not None:
        if "max_abs_constraint_residual" not in accepted:
            raise ValueError("CSV has no max_abs_constraint_residual column")
        accepted = accepted[accepted["max_abs_constraint_residual"].le(
            args.constraint)]
    accepted = accepted.sort_values(
        ["normalized_rms_geometric_deviation", "normalized_max_geometric_deviation"], kind="stable"
    )
    output = args.out or args.input_csv.with_name(
        args.input_csv.stem + "_filtered.csv")
    accepted.to_csv(output, index=False)
    print(f"accepted {len(accepted)} / {len(df)} rows -> {output}")


if __name__ == "__main__":
    main()
