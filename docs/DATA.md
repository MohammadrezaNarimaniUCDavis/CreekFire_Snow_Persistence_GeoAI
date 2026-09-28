# Data products

## Shipped on GitHub (`data/`)

| Path | Description |
| ---- | ----------- |
| `boundary/creek_fire_perimeter.gpkg` | Creek Fire perimeter (EPSG:32611-ready via GeoPandas) |
| `boundary/creek_fire_perimeter.geojson` | Same perimeter as GeoJSON |
| `boundary/creek_fire_attributes.json` | MTBS event metadata (name, ignition date, area) |
| `boundary/aoi_bbox.json` | Analysis AOI bounding box |
| `derived/matched_treated.parquet` | n = 3,778 matched burned cells + control indices / covariates |
| `derived/baci_panel.parquet` | Matched-pair annual panel (WY2016–2026) |
| `derived/baci_panel_with_sdd.parquet` | Panel with SDD-proxy fields |
| `derived/analysis_cells.parquet` | Full treated/control cell stack used to build matches |
| `derived/era5land_wy_aoi_means.csv` | ERA5-Land water-year AOI climate means |

## Zenodo-only supporting rasters

Distributed in `CreekFire_Snow_Persistence_GeoAI_supporting_rasters.zip`:

| Folder | Content |
| ------ | ------- |
| `hls_persist_500m/` | HLS NDSI snow-persistence GeoTIFFs (WY2016–2026, 500 m) |
| `modis_persist_500m/` | MODIS persistence cross-check stack |
| `sdd_500m/` | Snow-disappearance-day proxy rasters |
| `dem/` | Copernicus DEM clip for the AOI |
| `severity/` | Sentinel-2 dNBR severity at 500 m |

## Source licenses (summary)

| Source | Role | License / terms |
| ------ | ---- | ---------------- |
| NASA HLS (HLSL30 / HLSS30) | Snow persistence | NASA open data / Earthdata terms |
| MODIS snow products | Cross-sensor validation | NASA open data |
| Sentinel-2 | Burn severity (dNBR) | Copernicus open access |
| Copernicus DEM | Terrain | Copernicus license |
| ERA5-Land | Winter climate | Copernicus CDS license |
| MTBS / fire perimeter | Event boundary | USGS / USFS public |

Redistribution here is for **scientific replication**. Downstream users must respect original provider terms.

## Coordinate reference

Analysis grid: **500 m**, projected CRS **EPSG:32611** (WGS 84 / UTM zone 11N).
