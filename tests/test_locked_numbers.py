from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]


def test_panel_shape_and_years():
    panel = pd.read_parquet(ROOT / "data" / "derived" / "baci_panel.parquet")
    assert panel["cell_id"].nunique() == 3778
    assert panel["water_year"].min() == 2016
    assert panel["water_year"].max() == 2026


def test_baci_summary_locked():
    baci = json.loads((ROOT / "results" / "statistical" / "baci_summary.json").read_text(encoding="utf-8"))
    assert baci["n_matched_cells"] == 3778
    assert abs(baci["baci_effect"] - 0.00171) < 5e-4


def test_best_model_r2():
    best = json.loads((ROOT / "results" / "metrics" / "best_model_spatial_cv.json").read_text(encoding="utf-8"))
    assert best["n"] == 22665
    assert best["r2"] > 0.80


def test_figures_present():
    fig = ROOT / "results" / "figures"
    for i in range(1, 10):
        assert (fig / f"figure_{i:02d}.png").exists()
