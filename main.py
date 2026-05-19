# 📊 Sales Data Cleaning Project using Python (Pandas)

## 🚀 Overview
This project demonstrates basic data cleaning and preprocessing using Python and Pandas.  
The dataset contains sales data which is cleaned by handling missing values, removing unnecessary columns, and preparing it for further analysis.

---

## 🛠️ Technologies Used
- Python 🐍
- Pandas 📊

---

## 📁 Project Structure
- sales2019.csv → Raw dataset  
- sales2019_cleaned.csv → Cleaned dataset  
- main.py → Python script for data cleaning  

---

## ⚙️ Data Cleaning Steps

### 1. Load Dataset
```python
import pandas as pd

df = pd.read_csv("sales2019.csv")
