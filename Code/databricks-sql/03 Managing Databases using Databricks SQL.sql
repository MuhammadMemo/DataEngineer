CREATE DATABASE IF NOT EXISTS lms_bronze;

CREATE DATABASE IF NOT EXISTS lms_silver;

SHOW DATABASES;

DESCRIBE DATABASE lms_bronze;
DESCRIBE DATABASE lms_silver;

CREATE DATABASE IF NOT EXISTS lms_gold LOCATION 'dbfs:/user/hive/warehouse/lms_gold.db';

DESCRIBE DATABASE lms_gold;

DROP DATABASE IF EXISTS lms_bronze CASCADE;
DROP DATABASE IF EXISTS lms_silver;

CREATE TABLE lms_bronze.dummy (i INT);

CREATE DATABASE IF NOT EXISTS lms_bronze
COMMENT 'LMS Bronze';

COMMENT ON DATABASE lms_silver IS 'LMS Silver';
