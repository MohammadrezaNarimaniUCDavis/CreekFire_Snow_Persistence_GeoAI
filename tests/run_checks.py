"""Plain checks for locked replication numbers (no pytest plugins required)."""
from __future__ import annotations

import json
import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    errors = []
    panel = pd.read_parquet(ROOT / "data" / "derived" / "baci_panel.parquet")
    if panel["cell_id"].nunique() != 3778:
        errors.append(f"matched cells != 3778 ({panel['cell_id'].nunique()})")
    if panel["water_year"].min() != 2016 or panel["water_year"].max() != 2026:
        errors.append("unexpected water-year range")

    baci = json.loads((ROOT / "results" / "statistical" / "baci_summary.json").read_text(encoding="utf-8"))
    if baci["n_matched_cells"] != 3778:
        errors.append("baci n mismatch")
    if abs(baci["baci_effect"] - 0.00171) > 5e-4:
        errors.append(f"baci effect drift: {baci['baci_effect']}")

    best = json.loads((ROOT / "results" / "metrics" / "best_model_spatial_cv.json").read_text(encoding="utf-8"))
    if best["n"] != 22665 or best["r2"] <= 0.80:
        errors.append(f"best model metrics unexpected: {best}")

    for i in range(1, 10):
        if not (ROOT / "results" / "figures" / f"figure_{i:02d}.png").exists():
            errors.append(f"missing figure_{i:02d}.png")

    if errors:
        print("FAIL:")
        for e in errors:
            print(" -", e)
        return 1
    print("OK: locked numbers and figures verified.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
