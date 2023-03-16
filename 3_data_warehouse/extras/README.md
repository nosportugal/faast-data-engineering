# Load directly to GCP

This is a quick hack to load files directly to GCS, without Airflow.

This script downloads `.csv` files from `https://github.com/DataTalksClub/nyc-tlc-data/releases/download/` and upload them to your Cloud Storage Account as parquet files.

1. Install requirements (more info in `web_to_gcs.py` script)
2. Run: `python web_to_gcs.py`
