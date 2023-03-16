# Week 3 Homework

In this homework, we will perform some queries on BigQuery as well as answer some theoretical questions.

## Question 1: What is the count for `fhv` vehicles data for the year 2019?

* 7778101
* 6785099
* 42084899
* 11876543

## Question 2 - How many distinct `dispatching_base_num` do we have in `fhv` for 2019?

* 1098
* 792
* 86
* 1

## Question 3 - What is the best strategy a table whose queries will always filter by `dropoff_datetime` and order by `dispatching_base_num`?

* Partition by `dropoff_datetime`
* Partition by `dispatching_base_num`
* Partition by `dropoff_datetime` and cluster by `dispatching_base_num`
* Partition by `dispatching_base_num` and cluster by `dropoff_datetime`

## Question 4 - What is the count, estimated and actual data processed for query which counts trip between `2019-01-01` and `2019-03-31` for `dispatching_base_num` B00987, B02060, B02279?

Create a table with optimized clustering and partitioning, and run a count(*). Estimated data processed can be found in top right corner and actual data processed can be found after the query is executed.

PS: Use best approximation for data processed values.

* Count: 0; Estimated data processed: 0 MB; Actual data processed: 600 MB
* Count: 26558; Estimated data processed: 400 MB; Actual data processed: 150 MB
* Count: 26558; Estimated data processed: 155 MB; Actual data processed: 400 MB
* Count: 26558; Estimated data processed: 600 MB; Actual data processed: 150 MB

## Question 5 - What would be the best partitioning or clustering strategy when filtering on `dispatching_base_num` and `SR_Flag`?

* Partition by `dispatching_base_num` and cluster by `SR_Flag`
* Partition by `SR_Flag` and cluster by `dispatching_base_num`
* Cluster by `dispatching_base_num` and partition by `SR_Flag`
* Partition by `dispatching_base_num` and cluster by `SR_Flag`

## Question 6 - What improvements can be seen by partitioning and clustering for a small data size (i.e. less than 1 GB)?

Partitioning and clustering also creates extra metadata. Before query execution this metadata needs to be processed.

* No improvements OR it can be worse due to the extra metadata
* No improvements but it can never be worse
* Huge improvement in data processed
* Huge improvement in query performance

## Question 7 - In which format does BigQuery save data?

* Parquet
* Columnar
* Row
