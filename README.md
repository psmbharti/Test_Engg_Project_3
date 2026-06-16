## Test Tech Validation Project

This project demonstrates all 8 responsibilities:

Requirement	Project Activity
1. SQL & Database Concepts	Store test results in MySQL
2. System Validation & Equipment Setup	Verify devices before testing
3. Linux & Python Operations	Run commands and automation scripts
4. Assist with Validation Setup	Prepare test environment
5. Functional & Reliability Testing	Execute hardware tests
6. Python Automation	Analyze and process results
7. Documentation	Save results in database
8. Troubleshooting & Improvement	Identify failures and trends

Project Architecture
Hardware Device
       ↓
Validation Setup
       ↓
Functional Testing
       ↓
Reliability Testing
       ↓
Python Automation
       ↓
SQL Database
       ↓
KPI Analysis
       ↓
Excel Dashboard 
       ↓
Engineer Review

Hardware-Test-Validation-System/
│
├── data/
│   ├── test_data.csv
│
├── sql/
│   ├── create_database.sql
│   ├── analysis_queries.sql
│
├── python/
│   ├── test_analysis.py
│   ├── generate_report.py
│
├── dashboard/
│   ├── Excel_Dashboard.xlsx
│  
│
├── screenshots/
│   ├── dashboard.png
│
├── README.md


# Step 1: Create MySQL Database

# Step 2: Import Dataset in MySql

# Step 3: System Validation & Equipment Setup

Before testing:

Equipment Checklist
Power Supply
Test Router
Test Server
Linux Test Machine
Test Scripts
Network Connection

Example:

Device Connected ✓
Power Available ✓
WiFi Available ✓
Test Script Loaded ✓

This ensures a stable test environment.

# Step 4: Functional Testing

Check:

Power Test
Device Boots Correctly
WiFi Test
Device Connects to Network
Camera Test
Image Captured Successfully

Results:

Pass / Fail

# Step 5: Reliability Testing

Run device repeatedly.

Example:

100 Reboot Cycles
24 Hour Run Test
Stress Testing

Purpose:

Find intermittent failures

# Step 6: Linux Operations
 
 commands used by Test Technicians:

For Check files 
 ls

For Current location:
 pwd

View logs:  
 Create a Sample Log File

Linux:
echo "Test Started" > log.txt
echo "Device D001 Passed" >> log.txt
echo "Device D002 Failed WiFi Test" >> log.txt

View the file:
cat log.txt

Test Tech Use cat

Command	               Purpose
cat log.txt	         Display entire log
tail log.txt	         View latest entries
tail -f log.txt	   Monitor live logs
grep FAIL log.txt	 Find failures
wc -l log.txt	        Count log lines

Example:

grep FAIL test_log.txt

Output:

2026-01-01 08:12:00 Device D002 WiFi Test FAIL

This is a common activity for Test Tech when troubleshooting failed hardware tests and reporting issues to engineers.

Check processes:
  ps

Disk usage:
  df -h

# Step 7: Python Automation

Read CSV and calculate KPIs.(python.py)

# Step 8: SQL Analysis
Total Tests
Pass Rate
Failures by Equipment
Top Issues

# KPI Dashboard

Created in Excel .

KPI Cards
Total Tests
=COUNTA(A2:A201)
Passed Tests
=COUNTIF(K2:K201,"Pass")
Failed Tests
=COUNTIF(K2:K201,"Fail")
Pass Rate %
=Passed/Total

Dashboard Visuals
Pass vs Fail
Failures by Equipment
Issues by Category
Tests Over Time

Brief Explanation of Requirements 1–8

1. SQL and Database Concepts

Store test results, run queries, generate reports.

2. System Validation and Equipment Setup

Prepare devices and equipment before testing.

3. Linux and Python Operations

Use Linux commands and Python scripts for automation.

4. Assist with Validation Setup

Configure test stations and verify readiness.

5. Functional and Reliability Testing

Check device functionality and long-term stability.

6. Execute Linux Commands and Python Scripts

Collect logs, automate tests, and analyze results.

7. Document Results and Report Issues

Save findings in SQL and communicate failures.

8. Troubleshooting and Continuous Improvement

Identify root causes and recommend fixes.