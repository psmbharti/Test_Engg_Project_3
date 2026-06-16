# test_analysis.py (Analyze raw test data and identify failures)

# For total
# import pandas as pd

# df = pd.read_csv(r"C:\Users\madhu\OneDrive\Desktop\Python\GITHUB_Resume_Projects\Test Engg\test_validation_project\test_data.csv")

# total = len(df)
# passed = len(df[df["Overall_Result"]=="Pass"])
# failed = len(df[df["Overall_Result"]=="Fail"])

# print("Total:", total)
# print("Passed:", passed)
# print("Failed:", failed)

import pandas as pd

# Load dataset
df = pd.read_csv(r"C:\Users\madhu\OneDrive\Desktop\Python\GITHUB_Resume_Projects\Test Engg\test_validation_project\Data\test_data.csv")


# Display first 10 recordse
print("\nFIRST 10 RECORDS")
print(df.head(10))

# Total tests
print("\nTOTAL TESTS")
print(len(df))

# Pass/Fail Summary
print("\nPASS FAIL SUMMARY")
print(df["Overall_Result"].value_counts())

# Equipment Summary
print("\nTESTS BY EQUIPMENT")
print(df["Equipment"].value_counts())

# Failed Devices
failed = df[df["Overall_Result"] == "Fail"]

print("\nFAILED DEVICES")
print(failed[["Device_ID", "Equipment", "Issue"]])

# Top Issues
print("\nTOP ISSUES")
print(df["Issue"].value_counts())

# Reliability Test Summary
print("\nRELIABILITY TEST RESULTS")
print(df["Reliability_Test"].value_counts())

print("\nAnalysis Complete")