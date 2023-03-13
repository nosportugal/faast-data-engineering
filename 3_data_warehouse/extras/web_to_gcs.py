import io
import os
import requests
import pandas as pd
import pyarrow

from pathlib import Path
from google.cloud import storage

"""
Pre-reqs: 
1. `pip install requests pandas pyarrow google-cloud-storage` in your virtual env
  or DockerFile
2. Set GOOGLE_APPLICATION_CREDENTIALS to your project/service-account key 
  OR run "gcloud auth application-default login" in your terminal to authenticate
3. Set GCP_GCS_BUCKET as your bucket or change default value of BUCKET
"""

init_url = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/"

# Add GCP project and bucket name
PROJECT_ID = os.environ.get("GCP_PROJECT", "faast-data-engineering")
BUCKET = os.environ.get("GCP_GCS_BUCKET", "gcs-faast-data-engineering")


STANDARD_DTYPES = {
    "Unnamed: 0": "int",
    "VendorID": "float",
    "store_and_fwd_flag": "object",
    "RatecodeID": "float",
    "PULocationID": "int",
    "DOLocationID": "int",
    "passenger_count": "float",
    "trip_distance": "float",
    "fare_amount": "float",
    "extra": "float",
    "mta_tax": "float",
    "tip_amount": "float",
    "tolls_amount": "float",
    "ehail_fee": "float",
    "improvement_surcharge": "float",
    "total_amount": "float",
    "payment_type": "float",
    "trip_type": "float",
    "congestion_surcharge": "float",
}

FHV_DTYPES = {
    "dispatching_base_num": "object",
    "pickup_datetime": "object",
    "dropoff_datetime": "object",
    "PUlocationID": "float64",
    "DOlocationID": "float64",
    "SR_Flag": "float64",
    "Affiliated_base_number": "object",
}


DTYPES = {
    "green": STANDARD_DTYPES,
    "yellow": STANDARD_DTYPES,
    "fhv": FHV_DTYPES,
}


def upload_to_gcs(bucket, object_name, local_file):
    """
    Ref: https://cloud.google.com/storage/docs/uploading-objects#storage-upload-object-python
    """
    # # WORKAROUND to prevent timeout for files > 6 MB on 800 kbps upload speed.
    # # (Ref: https://github.com/googleapis/python-storage/issues/74)
    # storage.blob._MAX_MULTIPART_SIZE = 5 * 1024 * 1024  # 5 MB
    # storage.blob._DEFAULT_CHUNKSIZE = 5 * 1024 * 1024  # 5 MB

    client = storage.Client(project=PROJECT_ID)
    bucket = client.bucket(bucket)
    blob = bucket.blob(object_name)
    blob.upload_from_filename(local_file)


def web_to_gcs(year, service):
    for month in range(1, 13):
        # Get file name
        output_dir = Path(f"{service}/")
        output_dir.mkdir(parents=True, exist_ok=True)
        file_name = output_dir / f"{service}_tripdata_{year}-{month:0>2}.csv.gz"

        # Download and save
        request_url = init_url + file_name.as_posix()
        response = requests.get(request_url)
        fp = io.BytesIO(response.content)
        print(f"Local: {file_name}")

        # Fix column types and save into a parquet file
        df = pd.read_csv(
            fp, dtype=DTYPES[service], compression="gzip", encoding="latin1"
        )
        file_name = file_name.as_posix().replace(".csv.gz", ".parquet")
        df.to_parquet(file_name, engine="pyarrow")
        print(f"Parquet: {file_name}")

        # Upload it to GCS
        upload_to_gcs(BUCKET, f"{service}/{file_name}", file_name)
        print(f"GCS: {service}/{file_name}")


if __name__ == "__main__":
    web_to_gcs("2019", "green")
    web_to_gcs("2020", "green")
    web_to_gcs("2019", "yellow")
    web_to_gcs("2020", "yellow")
    web_to_gcs("2019", "fhv")
