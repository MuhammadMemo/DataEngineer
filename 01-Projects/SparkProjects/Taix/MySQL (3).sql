-- Databricks notebook source
-- MAGIC %fs ls

-- COMMAND ----------

-- MAGIC %fs ls dbfs:/public/

-- COMMAND ----------

-- MAGIC %fs ls dbfs:/public/Taxi/

-- COMMAND ----------

SELECT * FROM text.`dbfs:/public/Taxi/yellow_tripdata_2022-01.parquet` limit 10

-- COMMAND ----------

SELECT * FROM parquet.`dbfs:/public/Taxi/yellow_tripdata_2022-01.parquet` limit 10

-- COMMAND ----------

show views

-- COMMAND ----------

drop view  taxi

-- COMMAND ----------

create or replace  view Taxi as
SELECT 
VendorID,
to_date(tpep_pickup_datetime,'yyyy-MM-dd') as pickup_date,
date_format(tpep_pickup_datetime, 'HH:mm:ss') as pickup_time,
date_format(tpep_pickup_datetime, 'HH') as pickup_Hour,
to_date(tpep_dropoff_datetime,'yyyy-MM-dd') as dropoff_date,
date_format(tpep_dropoff_datetime, 'HH:mm:ss') as dropoff_time,
date_format(tpep_dropoff_datetime, 'HH') as dropoff_Hour,
passenger_count,
trip_distance,
RatecodeID,
store_and_fwd_flag,
PULocationID,
DOLocationID,
payment_type,
fare_amount,
extra,
mta_tax,
tip_amount,
tolls_amount,
improvement_surcharge,
total_amount,
congestion_surcharge,
airport_fee
 FROM parquet.`dbfs:/public/Taxi/`


-- COMMAND ----------

describe Taxi

-- COMMAND ----------

SHOW COLUMNS in Taxi

-- COMMAND ----------

select * from Taxi limit 1000

-- COMMAND ----------

select count(*) from Taxi

-- COMMAND ----------

insert overwrite directory '/public/Taxi/'
USING PARQUET
select * from Taxi

-- COMMAND ----------

-- MAGIC %fs ls dbfs:/public/Taxi/

-- COMMAND ----------

SELECT count(*) FROM parquet.`dbfs:/public/Taxi/` limit 10

-- COMMAND ----------

set spark.sql.warehouse.dir 

-- COMMAND ----------

select current_database()

-- COMMAND ----------

create database taxi_DB

-- COMMAND ----------

use taxi_DB

-- COMMAND ----------

select current_database()

-- COMMAND ----------

describe database taxi_db

-- COMMAND ----------

Create Table TaxiLog
(
 VendorID long ,
 pickup_date date ,
 pickup_time string,
 dropoff_date date,
 dropoff_time string ,
 dropoff_Hour string ,
 passenger_count double ,
 trip_distance double ,
 RatecodeID double ,
 store_and_fwd_flag string ,
 PULocationID long ,
 DOLocationID long,
 payment_type long ,
 fare_amount double ,
 extra double ,
 mta_tax double ,
 tip_amount double ,
 tolls_amount double ,
 improvement_surcharge double ,
 total_amount double ,
 congestion_surcharge double ,
 airport_fee double
) using delta


-- COMMAND ----------

drop Table TaxiLog

-- COMMAND ----------

drop database taxi_DB cascade

-- COMMAND ----------

show views 'dbfs:/public/Taxi/'

-- COMMAND ----------

-- MAGIC %fs ls dbfs:/user/hive/warehouse
-- MAGIC

-- COMMAND ----------

REFRESH TABLE taxilog;

-- COMMAND ----------

copy into TaxiLog  FROM 'dbfs:/public/Taxi/' fileformat =parquet
FORMAT_OPTIONS ('mergeSchema' = 'true')
COPY_OPTIONS ('mergeSchema' = 'true');

-- COMMAND ----------

select * from TaxiLog

-- COMMAND ----------

select count(*) from TaxiLog

-- COMMAND ----------

show functions

-- COMMAND ----------

describe function substring

-- COMMAND ----------

describe function trim

-- COMMAND ----------


