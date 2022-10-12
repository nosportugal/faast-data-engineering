# Week 5 Homework

In this homework we'll put what we learned about Spark
in practice.

We'll use high volume for-hire vehicles (HVFHV) dataset for that.

## Question 1: Install Spark and PySpark

* Install Spark
* Run PySpark
* Create a local spark session
* Execute `spark.version`

What's the output?

## Question 2: HVFHW February 2021

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

What's the size of the folder with results (in MB)?

## Question 3: Count records

How many taxi trips were there on February 15?

Consider only trips that started on February 15.

## Question 4: Longest trip for each day

Now calculate the duration for each trip.

Trip starting on which day was the longest?

## Question 5: Most frequent `dispatching_base_num`

Now find the most frequently occurring `dispatching_base_num`
in this dataset.

How many stages this spark job has?

> Note: the answer may depend on how you write the query,
> so there are multiple correct answers.
> Select the one you have.

## Question 6: Most common locations pair

Find the most common pickup/drop-off pair.

For example:

"Jamaica Bay / Clinton East"

Enter two zone names separated by a slash

If any of the zone names are unknown (missing), use "Unknown". For example, "Unknown / Clinton East".

## Question 7: Join type

For finding the answer to Q6, you'll need to perform a join.

What type of join is it?

And how many stages your spark job has?

Here is the solution to questions: [video](https://youtu.be/3LK0elHi3fA)
