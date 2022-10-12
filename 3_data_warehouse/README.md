# Data Warehouse and BigQuery

[Slides](https://docs.google.com/presentation/d/1a3ZoBAXFk8-EhUsd7rAZd-5p_HpltkzSeujjRGB2TAI/edit?usp=sharing)  
[Big Query basic SQL](code/big_query.sql)

## Data Warehouse

[Data Warehouse and BigQuery](https://youtu.be/jrHljAoD6nM)

## Partitioning and clustering

[Partitioning and Clustering](https://youtu.be/jrHljAoD6nM?t=726)  
[Partitioning vs Clustering](https://youtu.be/-CqXf7vhhDs)  

## Best practices

[BigQuery Best Practices](https://youtu.be/k81mLJVX08w)  

## Internals of BigQuery

[Internals of BigQuery](https://youtu.be/eduHi1inM4s)  

## Advanced BigQuery

### ML

[BigQuery Machine Learning](https://youtu.be/B-WtpB0PuG4)  
[SQL for ML in BigQuery](code/big_query_ml.sql)

**Important links**:

- [BigQuery ML Tutorials](https://cloud.google.com/bigquery-ml/docs/tutorials)
- [BigQuery ML Reference Parameter](https://cloud.google.com/bigquery-ml/docs/analytics-reference-patterns)
- [Hyper Parameter tuning](https://cloud.google.com/bigquery-ml/docs/reference/standard-sql/bigqueryml-syntax-create-glm)
- [Feature preprocessing](https://cloud.google.com/bigquery-ml/docs/reference/standard-sql/bigqueryml-syntax-preprocess-overview)

#### Deploying ML model

[BigQuery Machine Learning Deployment](https://youtu.be/BjARzEWaznU)  
[Steps to extract and deploy model with docker](extract_model.md)  

## [Workshop](code/airflow/README.md.md)

- [Integrating BigQuery with Airflow (+ Week 2 Review) - Video](https://www.youtube.com/watch?v=lAxAhHNeGww&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=31)

- Setup:
  Copy over the `code/airflow` directory (i.e. the Dockerized setup) from `week_2_data_ingestion`:

  ```bash
  cp ../week_2_data_ingestion/code/airflow airflow
  ```

  Also, empty the `logs` directory, if you find it necessary.

- DAG: [gcs_to_bq_dag.py](code/airflow/dags/gcs_to_bq_dag.py)

## Homework

This week's homework will have you writing queries to answer a variety of questions.

More information [here](homework.md)

- [Homework](homework.md)
- [Office Hours](https://youtu.be/U7iBBV8Dn74)
  - How to data changes in a data warehouse?
  - AWS vs GCP
  - Use cases for Kubernetes in DE
