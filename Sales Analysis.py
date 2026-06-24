import pandas as pd
import numpy as np

df = pd.read_csv("data.csv.csv")

print("Original Data:")
print(df)

df = df.dropna()
df = df.drop_duplicates()

df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)

df["Sales"] = df["Quantity"] * df["Price"]

df["Month"] = df["Date"].dt.month_name()

print("\nProcessed Data:")
print(df)

print("\nTotal rows after cleaning:", len(df))

monthly_sales = df.groupby("Month")["Sales"].sum()

print("\nMonthly Sales Report:")
print(monthly_sales)

top_products = df.groupby("Product")["Sales"].sum().sort_values(ascending=False)

print("\nTop Products:")
print(top_products.head(10))

top_customers = df.groupby("Customer")["Sales"].sum().sort_values(ascending=False)


