# Week 4 Homework

In this homework, we'll use the models developed during the week 4 videos and enhance the already presented dbt project using the already loaded Taxi data for `fhv` vehicles for year 2019 in our DWH.

If you don't have access to GCP, you can do this locally using the ingested data from your Postgres database. If you have access to GCP, you don't need to do it for local Postgres - only if you want to.

To answer questions 1 and 2, you will need:

1. Complete the "Build the first dbt models" video
2. Complete the "Visualizing the data" video
3. Rerun the models with the test run variable disabled

## Question 1 - What are the count of records in the model fact_trips after running green and yellow trip models with the test run variable disabled and filtering for 2019 and 2020 data only (pickup datetime)?

* 43195059
* 51340716
* 36472317
* 43193765

## Question 2 - What are the distribution between service type filtering by years 2019 and 2020 data as done in the videos?

Use your dashboard with the updated data from the previous question to answer this question.

* 85.9% Yellow - 14.1% Green
* 50.1% Yellow - 49.9% Green
* 95.1% Yellow - 49.9% Green
* 70.1% Yellow - 29.9% Green

To answer the questions 3, 4 and 5, you will need:

1. Create a staging model for the `fhv` data for 2019. Use the column `dispatching_base_num` and `pickup_datetime` as a surrogate key, remove rows where `dispatching_base_num` are null do not add a deduplication step. Run it via the CLI without limits (is_test_run: false).
2. Create a core model for the `stg_fhv_tripdata` joining with dim_zones. Call it `fact_fhv_trips`. Similar to what we've done in `fact_trips`, keep only records with known pickup and drop-off locations entries for pickup and drop-off locations. Run it via the CLI without limits (is_test_run: false) and filter records with pickup time in year 2019.

## Question 3 - What is the count of records in the model `stg_fhv_tripdata` after running all models with the test run variable disabled?

* 43244693
* 31994188
* 36786156
* 52608986

## Question 4 - What is the count of records in the model `fact_fhv_trips` after running all dependencies with the test run variable disabled?

* 47569094
* 37176147
* 22998722
* 12752253

## Question 5 - What is the month with the biggest amount of rides after building a tile for the `fact_fhv_trips` table?

Create a dashboard with some tiles that you find interesting to explore the data. One tile should show the number of trips per month, as done in the videos for fact_trips, based on the `fact_fhv_trips` table.

* January
* April
* October
* December
