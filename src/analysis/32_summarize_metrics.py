"""Print locked ML / SHAP / validation headline metrics from shipped results."""
from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
METRICS = ROOT / "results" / "metrics"


def main() -> None:
    best = json.loads((METRICS / "best_model_spatial_cv.json").read_text(encoding="utf-8"))
    shap = pd.read_csv(METRICS / "xgboost_shap_importance.csv")
    models = pd.read_csv(METRICS / "model_comparison_spatial_cv.csv")
    val = pd.read_csv(METRICS / "hls_modis_persist_validation.csv")

    elev_t = float(
        shap.loc[shap["feature"].isin(["elevation", "winter_tmean"]), "mean_abs_shap"].sum()
    )
    total = float(shap["mean_abs_shap"].sum())
    share = 100.0 * elev_t / total if total else float("nan")

    print("=== Locked GeoAI headlines ===")
    print(f"Best model: {best['model']} / {best['ablation']}")
    print(f"Spatial-CV R2 (level): {best['r2']:.3f}  RMSE={best['rmse']:.4f}  n={best['n']}")
    if "r2" in models.columns:
        print(models.to_string(index=False))
    print(f"SHAP elevation+winter_tmean share: {share:.1f}%")
    print("HLS–MODIS validation (head):")
    print(val.head().to_string(index=False))


if __name__ == "__main__":
    main()
