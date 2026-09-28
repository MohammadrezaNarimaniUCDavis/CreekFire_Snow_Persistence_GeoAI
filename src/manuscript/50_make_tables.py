"""Refresh manuscript CSV tables from locked statistical / metric products."""
from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
STAT = ROOT / "results" / "statistical"
MET = ROOT / "results" / "metrics"
OUT = ROOT / "results" / "tables"
OUT.mkdir(parents=True, exist_ok=True)


def main() -> None:
    baci = json.loads((STAT / "baci_summary.json").read_text(encoding="utf-8"))
    by_sev = pd.read_csv(STAT / "baci_by_severity.csv")
    balance = pd.read_csv(STAT / "matching_balance.csv")
    models = pd.read_csv(MET / "model_comparison_spatial_cv.csv")
    ablations = pd.read_csv(MET / "ablation_spatial_cv.csv")
    shap = pd.read_csv(MET / "xgboost_shap_importance.csv")

    rows = [
        {
            "quantity": "Overall BACI (persistence fraction)",
            "estimate": baci["baci_effect"],
            "ci95_low": baci["ci95_low"],
            "ci95_high": baci["ci95_high"],
            "n_cells": baci["n_matched_cells"],
        }
    ]
    for _, r in by_sev.iterrows():
        rows.append(
            {
                "quantity": f"BACI by severity ({r['severity']})",
                "estimate": r["baci_effect"],
                "ci95_low": None,
                "ci95_high": None,
                "n_cells": int(r["n_cells"]),
            }
        )
    pd.DataFrame(rows).to_csv(OUT / "table_03_baci_effects.csv", index=False)
    models.to_csv(OUT / "table_04_model_performance.csv", index=False)
    ablations.to_csv(OUT / "table_05_ablations.csv", index=False)
    balance.to_csv(OUT / "table_matching_balance.csv", index=False)
    shap.to_csv(OUT / "table_shap_importance.csv", index=False)
    print("Wrote manuscript tables to", OUT)


if __name__ == "__main__":
    main()
