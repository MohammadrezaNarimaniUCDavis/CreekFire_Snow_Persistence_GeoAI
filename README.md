# Creek Fire Snow Persistence GeoAI

Public replication package for a **multisource GeoAI** analysis of post-fire **snow persistence** after the **2020 Creek Fire** (Sierra Nevada, California).

> Farajpoor, P., & Narimani, M. (2026). *From Wildfire Severity to Snow Persistence: A Multisource GeoAI Study of the 2020 Creek Fire.* University of California, Davis.

**Authors:** Parastoo Farajpoor and Mohammadreza Narimani  
**Affiliation:** Department of Biological and Agricultural Engineering, UC Davis  
**Contact:** mnarimani@ucdavis.edu

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Dataset DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23024081.svg)](https://zenodo.org/records/23024081)

| Resource | Link |
| -------- | ---- |
| **Dataset (Zenodo)** | https://zenodo.org/records/23024081 |
| **This code** | https://github.com/MohammadrezaNarimaniUCDavis/CreekFire_Snow_Persistence_GeoAI |

This repository is the **public replication package**. It contains audited `.py` scripts and analysis-ready products needed to reproduce the paper's core BACI and GeoAI results. The authors' full working archive remains private.

**If you use this work, please cite the paper** (preferred once posted), plus the Zenodo dataset and/or this repository (see [Citation](#citation)).

---

## What this study does

1. Build a **500 m** matched burned-control panel for the Creek Fire using **HLS** NDSI snow persistence (WY2016-2026), **Sentinel-2** dNBR severity, Copernicus DEM terrain, and **ERA5-Land** winter climate.
2. Estimate **BACI** persistence effects overall and by severity class, with matching-balance diagnostics and event-study trajectories.
3. Compare nested **machine-learning** models under **spatial-block** cross-validation, with **SHAP** attribution (elevation + winter temperature dominate level prediction).
4. Keep sensor-cross checks (HLS-MODIS), SDD-proxy sensitivity, and GEDI context in a separate diagnostics track.

Claims are framed as **association / screening / spatially honest skill**, not causal parcel scores or operational snow forecasts.

### Locked headline numbers

| Metric | Value |
| ------ | ----- |
| Matched pairs (500 m cells) | **3,778** |
| Cell-years (ML panel) | **22,665** |
| Overall persistence BACI | **+0.0017** (95% CI 0.0003-0.0032) |
| High-severity BACI | **+0.026** |
| XGBoost level R^2 (spatial CV) | **0.811** |
| XGBoost anomaly R^2 (spatial CV) | **0.046** |
| SHAP share (elevation + winter T) | **~65.7%** |
| Grid / CRS | 500 m / **EPSG:32611** |

---

## Repository layout

```text
CreekFire_Snow_Persistence_GeoAI/
|-- config/                  # project + figure style
|-- data/
|   |-- boundary/            # Creek Fire perimeter + AOI (shipped)
|   |-- derived/             # analysis-ready panels (shipped)
|   `-- metadata/
|-- src/                     # audited replication code (.py)
|   |-- analysis/            # BACI recompute + metric summaries
|   |-- manuscript/          # table builders
|   |-- statistics/          # matching / BACI helpers
|   `-- utils/
|-- results/
|   |-- tables/              # manuscript tables
|   |-- statistical/         # BACI, event study, balance
|   |-- metrics/             # spatial CV, SHAP, OOF
|   `-- figures/             # Figures 01-09 (PNG + PDF)
|-- docs/
|-- tests/
|-- run_pipeline.py
|-- requirements.txt
|-- CITATION.cff
`-- LICENSE
```

Clipped HLS / MODIS / SDD / DEM / severity rasters are **not** stored on GitHub; they are distributed via Zenodo (see [Data availability](#data-availability)).

---

## Quick start

```bash
git clone https://github.com/MohammadrezaNarimaniUCDavis/CreekFire_Snow_Persistence_GeoAI.git
cd CreekFire_Snow_Persistence_GeoAI

conda create -n creek-snow-geoai python=3.11 -y
conda activate creek-snow-geoai
pip install -r requirements.txt

python src/analysis/31_recompute_baci.py
python src/analysis/32_summarize_metrics.py
python src/manuscript/50_make_tables.py
python tests/run_checks.py
```

Full acquisition (GEE HLS exports + supporting rasters): see [`docs/REPRODUCIBILITY.md`](docs/REPRODUCIBILITY.md) and [`docs/DATA.md`](docs/DATA.md).

```bash
python run_pipeline.py
```

---

## Data availability

| Product | GitHub | Zenodo |
| ------- | ------ | ------ |
| Creek Fire perimeter + AOI | yes | yes |
| Matched BACI panel (parquet) | yes | yes |
| Analysis cells + SDD-augmented panel | yes | yes |
| Manuscript tables + CV / SHAP diagnostics | yes | yes |
| Final figures (01-09) | yes | yes |
| OOF anomaly predictions | yes | yes |
| HLS / MODIS persistence, SDD, DEM, severity rasters | no | **yes** |

Modeled after the public replication style of [Palisades Urban Wildfire GeoAI](https://github.com/MohammadrezaNarimaniUCDavis/Palisades_Urban_Wildfire_GeoAI).

---

## Citation

**Preferred citation (paper):**

```bibtex
@article{Farajpoor_Narimani_CreekFire_Snow_2026,
  title   = {From Wildfire Severity to Snow Persistence: A Multisource GeoAI Study of the 2020 Creek Fire},
  author  = {Farajpoor, Parastoo and Narimani, Mohammadreza},
  year    = {2026},
  note    = {Department of Biological and Agricultural Engineering, University of California, Davis},
  url     = {https://github.com/MohammadrezaNarimaniUCDavis/CreekFire_Snow_Persistence_GeoAI}
}
```

**Dataset (Zenodo):**

```bibtex
@dataset{Farajpoor_Narimani_CreekFire_Snow_Persistence_GeoAI_2026,
  author    = {Farajpoor, Parastoo and Narimani, Mohammadreza},
  title     = {Creek Fire Snow Persistence GeoAI: analysis-ready panels, diagnostics, and supporting rasters for the 2020 Creek Fire},
  year      = {2026},
  version   = {1.0.0},
  publisher = {Zenodo},
  doi       = {10.5281/zenodo.23024081},
  url       = {https://zenodo.org/records/23024081}
}
```

**Replication code (this repository):**

```bibtex
@software{Farajpoor_Narimani_CreekFire_Snow_Persistence_GeoAI_code,
  author = {Farajpoor, Parastoo and Narimani, Mohammadreza},
  title  = {Creek Fire Snow Persistence GeoAI: replication code},
  year   = {2026},
  url    = {https://github.com/MohammadrezaNarimaniUCDavis/CreekFire_Snow_Persistence_GeoAI},
  note   = {Dataset DOI: https://zenodo.org/records/23024081}
}
```

GitHub's "Cite this repository" button uses [`CITATION.cff`](CITATION.cff).

---

## License

Code: MIT. Third-party geospatial inputs retain original licenses ([`docs/DATA.md`](docs/DATA.md), [`docs/NOTICE.md`](docs/NOTICE.md)).

---

## Contact

Mohammadreza Narimani - `mnarimani@ucdavis.edu` (University of California, Davis)
