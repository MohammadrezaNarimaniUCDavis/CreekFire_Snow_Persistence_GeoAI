# Reproducibility

## Reproduce headline numbers from shipped tables

With only the GitHub package (no GEE, no rasters):

```bash
pip install -r requirements.txt
python src/analysis/31_recompute_baci.py
python src/analysis/32_summarize_metrics.py
python src/manuscript/50_make_tables.py
python tests/run_checks.py
```

`31_recompute_baci.py` rebuilds overall BACI, severity-stratified BACI, and the event-study series from `data/derived/baci_panel.parquet` and writes refreshed files under `results/statistical/`.

`32_summarize_metrics.py` reads locked CV / SHAP / OOF products under `results/metrics/` and prints the manuscript headline block.

## Full stack (optional)

1. Download `CreekFire_Snow_Persistence_GeoAI_supporting_rasters.zip` from Zenodo and unpack into `data/supporting_rasters/`.
2. Confirm HLS WY GeoTIFFs exist under `data/supporting_rasters/hls_persist_500m/`.
3. Re-run matching / panel construction only if you intentionally change the grid or covariates (advanced; not required for table replication).

Earth Engine acquisition scripts used in the private working archive are **not** required to verify the paper's locked BACI and ML metrics.

## Environment

- Python 3.11 recommended
- See `requirements.txt` and `data/metadata/pip_freeze.txt`

## Design notes that protect against leakage

- Predictors for ML use **pre-fire** terrain, severity (static post-event map), years-since-fire, and winter climate - not post-fire recovery indices as outcomes mixed into features.
- Spatial-block CV is the primary generalization metric; random-split optimism is reported only as contrast.
- BACI uses **matched** burned-control pairs (n = 3,778).
