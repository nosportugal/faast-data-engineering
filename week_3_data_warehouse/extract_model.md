# Model deployment

This tutorial shows how to export a BigQuery ML model and then deploy the model either on AI Platform or on a local machine. You will use the iris table from the BigQuery public datasets and work through the following three end-to-end scenarios:

[Tutorial](https://cloud.google.com/bigquery-ml/docs/export-model-tutorial)

## Steps for model created in the video

```bash

gcloud auth login

bq --project_id taxi-rides-ny extract -m nytaxi.tip_model gs://taxi_ml_model/tip_model

mkdir /tmp/model

gsutil cp -r gs://taxi_ml_model/tip_model /tmp/model

mkdir -p serving_dir/tip_model/1

cp -r /tmp/model/tip_model/* serving_dir/tip_model/1

docker pull tensorflow/serving

docker run -p 8501:8501 --mount type=bind,source=`pwd`/serving_dir/tip_model,target=
  /models/tip_model -e MODEL_NAME=tip_model -t tensorflow/serving &

curl -d '{"instances": [{"passenger_count":1, "trip_distance":12.2, "PULocationID":"193", "DOLocationID":"264", "payment_type":"2","fare_amount":20.4,"tolls_amount":0.0}]}' -X POST <http://localhost:8501/v1/models/tip_model:predict> <http://localhost:8501/v1/models/tip_model>
```
