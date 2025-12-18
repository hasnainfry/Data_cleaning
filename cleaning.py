import pandas as pd


# Sample DataFrame

data = {
    "customer_id": [101, 102, 103, 104, 105, 106, 106],
    "name": ["Ali", "Sara", "Hassan", "Hina", "Usman", "Zara", "Zara"],
    "age": [25, None, 32, 22, None, 35, 35],
    "city": ["Lahore", "Karachi", None, "Lahore", "Islamabad", "Lahore", "Lahore"],
    "purchases": [3, 5, None, 2, 4, 6, 6],
    "total_amount": [20000, 45000, 30000, None, 50000, 70000, 70000]
}

df = pd.DataFrame(data)


# Q1 — Data Cleaning
# Fill missing 'age' with median
df["age"] = df["age"].fillna(df["age"].median())

# Fill missing 'purchases' with mean
df["purchases"] = df["purchases"].fillna(df["purchases"].mean())

# Fill missing 'city' with "Unknown"
df["city"] = df["city"].fillna("Unknown")


# Drop rows with missing total_amount

df.dropna(subset=["total_amount"], inplace=True)
print("Data after dropping rows with missing total_amount:\n", df)


# Remove Duplicates
print("Duplicate rows:\n", df.duplicated())
df.drop_duplicates(subset=["customer_id","name"], inplace=True)
print("Data after removing duplicates:\n", df)


# Filtering Insight
# Customers in Lahore with purchases >= 3
lahore_customers = df.loc[
    (df["city"] == "Lahore") & (df["purchases"] >= 3),
    ["name","age","purchases","total_amount"]
]
print("Lahore customers with purchases >= 3:\n", lahore_customers)


# Groupby + Sort

# Average total_amount per city sorted descending
city_avg_amount = df.groupby("city")["total_amount"].mean().sort_values(ascending=False)
print("Average total_amount per city (descending):\n", city_avg_amount)


#Final Cleaned CSV 

final_df = df[["customer_id","name","age","city","purchases","total_amount"]]
final_df.to_csv("cleaned_customer_data.csv", index=False)