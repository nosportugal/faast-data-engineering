# Week 5 Homework

In this homework we'll put what we learned about Spark in practice.

We'll use high volume for-hire vehicles (HVFHV) dataset for that.

## Spark and PySpark

* Install Spark
* Run PySpark
* Create a local spark session
* Execute `spark.version`

## HVFHW February 2021

Download the HVFHV data for February 2021:

```bash
wget https://d37ci6vzurychx.cloudfront.net/trip-data/fhvhv_tripdata_2021-02.parquet
```

Read it with Spark using the following schema

```python
from pyspark.sql import types


schema = types.StructType([
    types.StructField('hvfhs_license_num', types.StringType(), True),
    types.StructField('dispatching_base_num', types.StringType(), True),
    types.StructField('originating_base_num', types.StringType(), True),
    types.StructField('request_datetime', types.TimestampType(), True),
    types.StructField('on_scene_datetime', types.TimestampType(), True),
    types.StructField('pickup_datetime', types.TimestampType(), True),
    types.StructField('dropoff_datetime', types.TimestampType(), True),
    types.StructField('PULocationID', types.LongType(), True),
    types.StructField('DOLocationID', types.LongType(), True),
    types.StructField('trip_miles', types.DoubleType(), True),
    types.StructField('trip_time', types.LongType(), True),
    types.StructField('base_passenger_fare', types.DoubleType(), True),
    types.StructField('tolls', types.DoubleType(), True),
    types.StructField('bcf', types.DoubleType(), True),
    types.StructField('sales_tax', types.DoubleType(), True),
    types.StructField('congestion_surcharge', types.DoubleType(), True),
    types.StructField('airport_fee', types.DoubleType(), True),
    types.StructField('tips', types.DoubleType(), True),
    types.StructField('driver_pay', types.DoubleType(), True),
    types.StructField('shared_request_flag', types.StringType(), True),
    types.StructField('shared_match_flag', types.StringType(), True),
    types.StructField('access_a_ride_flag', types.StringType(), True),
    types.StructField('wav_request_flag', types.StringType(), True),
    types.StructField('wav_match_flag', types.StringType(), True),
])
```

We will use this dataset for all the remaining questions. Repartition it to 24 partitions and save it to parquet again.

## Question 1 - What is the size of the HVFHW February 2021 data?

What's the (approximate) size of the folder with results?

* 108 MB
* 158 MB
* 208 MB
* 258 MB

## Question 2 - How many taxi trips were there on February 15?

Consider only trips that started on February 15.

* 169840
* 264333
* 367170
* 462002

## Question 3 - Calculate the duration for each trip. When was the longest trip?

* 2021-02-11
* 2021-02-12
* 2021-02-13
* 2021-02-14

## Question 4 - What is the most frequent `dispatching_base_num`?

* B02512
* B0282
* B02764
* B02510

## Question 5 - What was the most common location pair?

Find the most common pickup/drop-off pair.

Enter two zone names separated by a slash. For example:

"Jamaica Bay / Clinton East"

If any of the zone names are unknown (missing), use "Unknown". For example, "Unknown / Clinton East".

* Brownsville / East New York
* East New York / East New York
* JFK Airport / Unknown
* Crown Heights North / Stuyvesant Heights

## Question 6 - To answer the previous question, you'll need to perform a join. What type of join strategy Spark will use?

* Shuffle join
* Broadcast join
* Shuffle hash join
* Shuffle sort merge join
