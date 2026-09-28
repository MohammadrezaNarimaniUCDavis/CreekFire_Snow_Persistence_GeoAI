"""Recompute locked BACI / event-study numbers from the shipped matched panel."""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
PANEL = ROOT / "data" / "derived" / "baci_panel.parquet"
OUT = ROOT / "results" / "statistical"
OUT.mkdir(parents=True, exist_ok=True)
RNG = np.random.default_rng(42)
N_BOOT = 500


def _baci(panel: pd.DataFrame) -> dict:
    pre = panel[panel["rel_year"] <= 0]["diff"]
    post = panel[panel["rel_year"] > 0]["diff"]
    pre_diff = float(np.nanmean(pre))
    post_diff = float(np.nanmean(post))
    effect = post_diff - pre_diff

    # Cell-level bootstrap on pair ids
    cells = panel["cell_id"].unique()
    boots = []
    for _ in range(N_BOOT):
        draw = RNG.choice(cells, size=len(cells), replace=True)
        sub = panel[panel["cell_id"].isin(draw)]
        boots.append(
            float(np.nanmean(sub.loc[sub["rel_year"] > 0, "diff"]))
            - float(np.nanmean(sub.loc[sub["rel_year"] <= 0, "diff"]))
        )
    boots = np.asarray(boots, dtype=float)
    return {
        "pre_diff": pre_diff,
        "post_diff": post_diff,
        "baci_effect": effect,
        "ci95_low": float(np.nanpercentile(boots, 2.5)),
        "ci95_high": float(np.nanpercentile(boots, 97.5)),
        "n_matched_cells": int(panel["cell_id"].nunique()),
        "resolution_m": 500.0,
        "snow_source": "GEE HLS HLSL30+HLSS30",
        "covariates": [
            "elevation",
            "slope",
            "northness",
            "eastness",
            "radiation_index",
            "pre_persist",
        ],
    }


def _by_severity(panel: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for sev, g in panel.groupby("sev_class"):
        pre = float(np.nanmean(g.loc[g["rel_year"] <= 0, "diff"]))
        post = float(np.nanmean(g.loc[g["rel_year"] > 0, "diff"]))
        rows.append(
            {
                "severity": sev,
                "n_cells": int(g["cell_id"].nunique()),
                "pre_diff": pre,
                "post_diff": post,
                "baci_effect": post - pre,
            }
        )
    return pd.DataFrame(rows).sort_values("severity")


def _event_study(panel: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for wy, g in panel.groupby("water_year"):
        d = g["diff"].to_numpy(dtype=float)
        est = float(np.nanmean(d))
        n = int(np.sum(np.isfinite(d)))
        se = float(np.nanstd(d, ddof=1) / np.sqrt(n)) if n > 1 else np.nan
        rows.append(
            {
                "water_year": int(wy),
                "rel_year": int(wy - 2020),
                "estimate": est,
                "se": se,
                "ci95_low": est - 1.96 * se if np.isfinite(se) else np.nan,
                "ci95_high": est + 1.96 * se if np.isfinite(se) else np.nan,
                "n": n,
            }
        )
    return pd.DataFrame(rows).sort_values("water_year")


def main() -> None:
    panel = pd.read_parquet(PANEL)
    summary = _baci(panel)
    (OUT / "baci_summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    _by_severity(panel).to_csv(OUT / "baci_by_severity.csv", index=False)
    _event_study(panel).to_csv(OUT / "event_study_persist.csv", index=False)
    print("BACI effect:", round(summary["baci_effect"], 5), "n=", summary["n_matched_cells"])
    print("Wrote:", OUT)


if __name__ == "__main__":
    main()
