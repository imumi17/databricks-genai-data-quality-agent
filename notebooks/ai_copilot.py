import pandas as pd

data = pd.read_csv("sample-data/Sales Dataset.csv")

missing_customer = data["CustomerName"].isnull().sum()
missing_state = data["State"].isnull().sum()

print("\n===== AI DATA QUALITY COPILOT =====\n")

if missing_customer > 0:
    print(
        f"""
Issue:
CustomerName contains {missing_customer} missing values.

Potential Root Cause:
Customer onboarding process may not be enforcing mandatory customer details.

Recommendation:
Implement mandatory field validation before data ingestion.
"""
    )

if missing_state > 0:
    print(
        f"""
Issue:
State contains {missing_state} missing values.

Potential Root Cause:
Regional information may be missing from source systems.

Recommendation:
Enhance source validation and reference data checks.
"""
    )

print("\n===== ANALYSIS COMPLETE =====")