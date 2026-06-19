## Test Tech Validation Project

====================
test_analysis.py' 
====================
FIRST 10 RECORDS
--------------------
  Test_ID       Date Device_ID  ... Reliability_Test Overall_Result         Issue
0    T001   1/2/2026      D001  ...             Pass           Pass           NaN
1    T002   1/3/2026      D002  ...             Pass           Pass           NaN
2    T003   1/4/2026      D003  ...             Pass           Pass           NaN
3    T004   1/5/2026      D004  ...             Pass           Pass           NaN
4    T005   1/6/2026      D005  ...             Pass           Fail  WiFi Failure
5    T006   1/7/2026      D006  ...             Pass           Fail  Script Error
6    T007   1/8/2026      D007  ...             Fail           Fail   Linux Error
7    T008   1/9/2026      D008  ...             Pass           Pass           NaN
8    T009  1/10/2026      D009  ...             Pass           Pass           NaN
9    T010  1/11/2026      D010  ...             Pass           Pass           NaN

[10 rows x 12 columns]

TOTAL TESTS
--------------------
200

PASS FAIL SUMMARY
--------------------
Overall_Result
Fail    121
Pass     79
Name: count, dtype: int64

TESTS BY EQUIPMENT
--------------------
Equipment
IoT_Device       47
Router           45
Switch           41
Server           35
Mobile_Device    32
Name: count, dtype: int64

FAILED DEVICES
--------------------
    Device_ID      Equipment          Issue
4        D005  Mobile_Device   WiFi Failure
5        D006         Router   Script Error
6        D007         Switch    Linux Error
11       D012     IoT_Device    Linux Error
12       D013         Router   Script Error
..        ...            ...            ...
191      D192  Mobile_Device    Linux Error
192      D193     IoT_Device   Script Error
197      D198         Server  Power Failure
198      D199     IoT_Device  Power Failure
199      D200  Mobile_Device    Linux Error

[121 rows x 3 columns]

TOP ISSUES
--------------------
Issue
WiFi Failure      32
Power Failure     27
Linux Error       26
Script Error      21
Camera Failure    15
Name: count, dtype: int64

RELIABILITY TEST RESULTS
--------------------
Reliability_Test
Pass    161
Fail     39
Name: count, dtype: int64

Analysis Complete
==================================================================================

=====================
generate_report.py' 
=====================



===========================
TEST VALIDATION REPORT
==========================
Total Tests  : 200
Passed Tests : 79
Failed Tests : 121
Pass Rate    : 39.5%

Equipment Failures
--------------------------------------------------
Equipment
Router           27
IoT_Device       26
Mobile_Device    24
Switch           23
Server           21
dtype: int64

Top Issues
--------------------------------------------------
Issue
WiFi Failure      32
Power Failure     27
Linux Error       26
Script Error      21
Camera Failure    15
Name: count, dtype: int64

Report Generated Successfully
==================================================================================

Analysis_Queries
====================
-- Total Tests
![alt text](image.png)

-- Pass Rate
![alt text](image-1.png)

-- Failures by Equipment
![alt text](image-2.png)

-- Top Issues
![alt text](image-3.png)

=================================================================================