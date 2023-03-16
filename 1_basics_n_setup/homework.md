# Week 1 Homework

In this homework we'll prepare the environment and practice with terraform and SQL

## Google Cloud SDK

Install Google Cloud SDK. What's the version you have?

To get the version, run `gcloud --version`

## Google Cloud account

Create an account in Google Cloud and create a project.

## Terraform

Now install terraform and go to the terraform directory (`1_basics_n_setup/code/1_terraform_gcp/terraform`)

After that, run

* `terraform init`
* `terraform plan`
* `terraform apply` and the confirm when prompted

## Prepare Postgres

Run Postgres and load data as shown in the videos

We'll use the yellow taxi trips from January 2021:

```bash
wget https://github.com/DataTalksClub/nyc-tlc-data/releases/download/yellow/yellow_tripdata_2020-01.csv.gz
```

You will also need the dataset with zones:

```bash
wget https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv
```

Download this data and put it to Postgres. Use SQL to answer the following questions.

## Question 1: Count records

How many taxi trips were there on January 15?

Consider only trips that started on January 15.

* 0
* 53024
* 534
* 53027

## Question 2: Largest tip for each day

Find the largest tip for each day. On which day it was the largest tip in January?

Use the pick up time for your calculations.

(note: it's not a typo, it's "tip", not "trip")

* 2021-01-20
* 2021-01-04
* 2021-01-01
* 2021-01-21

## Question 3: Most popular destination

What was the most popular destination for passengers picked up in central park on January 14?

Use the pick up time for your calculations.

Enter the zone name (not id). If the zone name is unknown (missing), write "Unknown"

* Upper East Side North
* Upper East Side South
* Unknown

## Question 4: Most expensive locations

What's the pickup/drop-off pair with the largest average price for a ride (calculated based on `total_amount`)?

Enter two zone names separated by a slash

For example:

"Jamaica Bay / Clinton East"

If any of the zone names are unknown (missing), write "Unknown". For example, "Unknown / Clinton East".

* Union Sq./Canarsie
* Borough Park/NV
* Alphabet City/Unknown
* Central Park/Upper East Side North
