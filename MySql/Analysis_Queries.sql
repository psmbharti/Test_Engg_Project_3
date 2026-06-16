## Step 8: SQL Analysis
-- Total Tests
SELECT COUNT(*) AS Total_Tests
FROM test_results;

-- Pass Rate
SELECT
COUNT(*) AS Total,
SUM(Overall_Result='Pass') AS Passed
FROM test_results;

-- Failures by Equipment
SELECT Equipment,
COUNT(*) AS Failures
FROM test_results
WHERE Overall_Result='Fail'
GROUP BY Equipment;

-- Top Issues
SELECT Issue,
COUNT(*) AS Occurrences
FROM test_results
GROUP BY Issue
ORDER BY Occurrences DESC;

