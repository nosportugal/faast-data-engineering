# The NYC Taxi dataset

[Medium article](https://medium.com/@NYCTLC/what-makes-a-city-street-smart-23496d92f60d)

[Trip record user guide](https://www1.nyc.gov/assets/tlc/downloads/pdf/trip_record_user_guide.pdf)

The data set is divided into 4 parts:

- Yellow cabs
- Green cabs
- For Hire Vehicles
- High volume for hire vehicles

Below you can see the data dictionary for Yellow and Green cabs.

## Yellow and Green cabs

| Columns               | Definition                                                                         | Example             |
| --------------------- | ---------------------------------------------------------------------------------- | ------------------- |
| VendorID              | A code indicating the TPEP provider that provided the record.                      | 2                   |
| lpep_pickup_datetime  | The date and time when the meter was engaged.                                      | 2021-01-01 00:15:56 |
| lpep_dropoff_datetime | The date and time when the meter was disengaged.                                   | 2021-01-01 00:19:52 |
| store_and_fwd_flag    | This flag indicates whether the trip record was held in vehicle memory before sending to the vendor because the vehicle did not have a connection to the server.| N,                  |
| RatecodeID            | The final rate code in effect at the end of the trip.                              | 1                   |
| PULocationID          | TLC Taxi Zone in which the taximeter was engaged.                                  | 43                  |
| DOLocationID          | TLC Taxi Zone in which the taximeter was disengaged.                               | 151                 |
| passenger_count       | The number of passengers in the vehicle. This is a driver-entered value.           | 1                   |
| trip_distance         | The elapsed trip distance in miles reported by the taximeter.                      | 1.01                |
| fare_amount           | The time-and-distance fare calculated by the meter.                                | 5.5                 |
| extra                 | Miscellaneous extras and                                                           | 0.5                 |
| mta_tax               | MTA tax amount that is automatically triggered based on the metered rate in use.                    | 0.5                 |
| tip_amount            | Tip amount – This field is automatically populated for credit card tips. Cash tips are not included.| 0                   |
| tolls_amount          | Total amount of all tolls paid in trip.                                            | 0                   |
| ehail_fee             |                                                                                    |                     |
| improvement_surcharge | Improvement surcharge amount. The improvement surcharge began being levied in 2015.| 0.3                 |
| total_amount          | The total amount charged to passengers. Does not include cash tips.                | 6.8                 |
| payment_type          | = Credit , 2= Cash, 3= No charge, 4= Dispute, 5= Unknown, 6= Voided trip           | 2                   |
| trip_type             | 1= Street-hail, 2= Dispatch                                                        | 1                   |
| congestion_surcharge  |                                                                                    | 0                   |

### Taxi zone Lookup

| Columns      | Definition | Example        |
| ------------ | ---------- | -------------- |
| LocationID   |            | 1              |
| Borough      |            | EWR            |
| Zone         |            | Newark Airport |
| service_zone |            | EWR            |

> **Note**: NYC TLC changed the format of the data we use to parquet. But you can still access the csv files [here](https://github.com/DataTalksClub/nyc-tlc-data). Alternatively, you can use the original parquet files at NYC TLC's [website](https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page) and then adapt your code to read parquets instead of csv.

[Taxi zones](https://data.cityofnewyork.us/Transportation/NYC-Taxi-Zones/d3c5-ddgc)

> **Warning**: At some points in the videos and code, you may see data being downloaded from an Amazon S3 bucket. This bucket, however, is no longer accessible. Please use the [GitHub backup](https://github.com/DataTalksClub/nyc-tlc-data) instead.

When you're ready, get over to [Week 1: Introduction & Prerequisites](week_1_basics_n_setup) to continue.
