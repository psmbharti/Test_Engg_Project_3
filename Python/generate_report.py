# generate_report.py(Generate KPI summary report for engineers/managers)

import pandas as pd

# Load dataset
df = pd.read_csv(r"C:\Users\madhu\OneDrive\Desktop\Python\GITHUB_Resume_Projects\Test Engg\test_validation_project\Data\test_data.csv")


# KPIs
total_tests = len(df)
passed = len(df[df["Overall_Result"] == "Pass"])
failed = len(df[df["Overall_Result"] == "Fail"])

pass_rate = round((passed / total_tests) * 100, 2)

# Equipment failures
equipment_failures = (
    df[df["Overall_Result"] == "Fail"]
    .groupby("Equipment")
    .size()
    .sort_values(ascending=False)
)

# Report
print("=" * 50)
print("TEST VALIDATION REPORT")
print("=" * 50)

print(f"Total Tests  : {total_tests}")
print(f"Passed Tests : {passed}")
print(f"Failed Tests : {failed}")
print(f"Pass Rate    : {pass_rate}%")

print("\nEquipment Failures")
print("-" * 50)
print(equipment_failures)

print("\nTop Issues")
print("-" * 50)
print(df["Issue"].value_counts())

print("\nReport Generated Successfully")