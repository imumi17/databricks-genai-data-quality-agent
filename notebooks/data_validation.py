import pandas as pd

df = pd.read_csv("sample-data/Sales Dataset.csv")

print("\n===== Missing Customer Names =====")
print(df[df["CustomerName"].isnull()])

print("\n===== Missing States =====")
print(df[df["State"].isnull()])

print("\n===== Total Records =====")
print(len(df))

print("\n===== Total Missing Names =====")
print(df["CustomerName"].isnull().sum())

print("\n===== Total Missing States =====")
print(df["State"].isnull().sum())