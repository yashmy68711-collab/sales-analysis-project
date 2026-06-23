import pandas as pd
import numpy as np

df = pd.read_csv("data.csv.csv")

print("Original Data:")
print(df)

df = df.dropna()

df = df.drop_duplicates()

df["Date"] = pd.to_datetime(df["Date"])

df["Sales"] = df["Quantity"] * df["Price"]

df["Month"] = df["Date"].dt.month_name()

print("\nProcessed Data:")
print(df)

print("\nTotal rows after cleaning:", len(df))
