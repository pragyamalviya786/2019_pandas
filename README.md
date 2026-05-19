# 📊 Sales Data Cleaning Project using Python (Pandas)

## 🚀 Overview
This project demonstrates basic data cleaning and preprocessing using Python and Pandas.  
The dataset contains sales data which is cleaned by handling missing values, removing unnecessary columns, and preparing it for further analysis.

---

## 🛠️ Technologies Used
- Python 🐍  
- Pandas 📊  

---

## 📁 Project Files
- sales2019.csv → Raw dataset  
- sales2019_cleaned.csv → Cleaned dataset  
- main.py → Python script for data cleaning  
- 2019_sales.png → Output screenshot  

---

## ⚙️ Data Cleaning Code

```python
import pandas as pd

# Load dataset
df = pd.read_csv("sales2019.csv")

# Data exploration
print(df.head())
print(df.shape)
print(df.info())
print(df.isnull().sum())

# Remove unnecessary columns
df.drop(columns=["promo_bin_2", "promo_discount_2", "promo_type_2"], inplace=True)

# Handle missing values
df["promo_bin_1"] = df["promo_bin_1"].fillna("No Promo")

# Save cleaned dataset
df.to_csv("sales2019_cleaned.csv", index=False)

print("Dataset cleaned successfully")
