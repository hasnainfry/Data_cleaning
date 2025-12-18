# Data_cleaning
# Customer Data Cleaning with Pandas 🐼

## Overview 📊
This repository demonstrates **real-world data cleaning and analysis** using Python's Pandas library.  
We practice **handling missing data, removing duplicates, filtering, and aggregating insights** on a sample customer dataset.

## Dataset 🗂️
Columns:
- `customer_id`: Unique ID of the customer
- `name`: Customer's name
- `age`: Age of the customer
- `city`: City of residence
- `purchases`: Number of purchases made
- `total_amount`: Total amount spent

## Tasks ✅
1. **Data Cleaning** 🧹
   - Fill missing `age` values with median
   - Fill missing `purchases` with mean
   - Fill missing `city` with "Unknown"

2. **Row Removal** ✂️
   - Drop rows with missing `total_amount`

3. **Duplicate Handling** 🔍
   - Remove duplicate rows based on `customer_id` and `name`

4. **Insights** 💡
   - Filter: Customers in Lahore with purchases ≥ 3
   - Groupby: Average `total_amount` per city, sorted descending

5. **Save Cleaned Data** 💾
   - Final cleaned DataFrame saved as `cleaned_customer_data.csv`

## How to Run ▶️
```bash
pip install pandas
python customer_data_cleaning.py
