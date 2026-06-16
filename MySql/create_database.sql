## Step 1: Create MySQL Database
CREATE DATABASE test_validation;
USE test_validation;

-- Create table:
CREATE TABLE test_results (
    Test_ID VARCHAR(10),
    Test_Date DATE,
    Device_ID VARCHAR(10),
    Equipment VARCHAR(50),
    Power VARCHAR(10),
    WiFi VARCHAR(10),
    Camera VARCHAR(10),
    Linux_Check VARCHAR(10),
    Python_Script VARCHAR(10),
    Reliability_Test VARCHAR(10),
    Overall_Result VARCHAR(10),
    Issue VARCHAR(50)
);

## Step 2: Import Dataset

SHOW VARIABLES LIKE 'secure_file_priv';

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/test_data.csv'
INTO TABLE test_results
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(
    Test_ID,
    @Test_Date,
    Device_ID,
    Equipment,
    Power,
    WiFi,
    Camera,
    Linux_Check,
    Python_Script,
    Reliability_Test,
    Overall_Result,
    Issue
)
SET Test_Date = STR_TO_DATE(@Test_Date, '%m/%d/%Y');

SELECT * FROM test_results;

-- Verify records.
SELECT COUNT(*) FROM test_results;


