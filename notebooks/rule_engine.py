import pandas as pd

data = pd.read_csv("sample-data/Sales Dataset.csv")
rules = pd.read_csv("sample-data/dq_rules.csv")

total_issues = 0

print("\n=== DATA QUALITY REPORT ===\n")

for _, rule in rules.iterrows():

    column = rule["column_name"]

    if rule["rule"] == "not_null":

        missing_count = data[column].isnull().sum()

        print(f"{column}: {missing_count} missing values")

        total_issues += missing_count

print("\n===========================")
print(f"Total Issues Found: {total_issues}")

quality_score = round(
    (1 - total_issues / (len(data) * len(rules))) * 100,
    2
)

print(f"Quality Score: {quality_score}%")