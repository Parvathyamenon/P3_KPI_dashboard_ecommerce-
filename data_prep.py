# FILE: data_prep.py
# PURPOSE: Clean Superstore data and calculate KPIs for Tableau dashboard

import pandas as pd
import numpy as np
import os

# -----------------------------
# Load dataset
# -----------------------------

df = pd.read_csv(
    r'c:\Users\PARVATHY\Desktop\projects\p3_KPI+dashboard\data\superstore.csv',
    encoding='utf-8-sig'   
)

# Clean column names
df.columns = df.columns.str.strip()

print("Columns:", df.columns.tolist())
print("Rows:", len(df))


# -----------------------------
# Fix dates
# -----------------------------

df['Order Date'] = pd.to_datetime(df['Order Date'], dayfirst=True, errors='coerce')
df['Ship Date']  = pd.to_datetime(df['Ship Date'], dayfirst=True, errors='coerce')

df['Year']        = df['Order Date'].dt.year
df['Month']       = df['Order Date'].dt.to_period('M').astype(str)
df['Quarter']     = df['Order Date'].dt.to_period('Q').astype(str)

df['Days to Ship'] = (df['Ship Date'] - df['Order Date']).dt.days


# -----------------------------
# Profit margin KPI
# -----------------------------

df['Profit Margin %'] = np.where(
    df['Sales'] > 0,
    df['Profit'] / df['Sales'] * 100,
    0
).round(2)


# -----------------------------
# Customer Lifetime Value
# -----------------------------

clv = df.groupby('Customer Name').agg(
    Total_Revenue=('Sales','sum'),
    Total_Profit=('Profit','sum'),
    Order_Count=('Order ID','nunique'),
    Avg_Order_Value=('Sales','mean')
).reset_index()

clv.columns = ['Customer Name','CLV','Profit_LTV','Orders','AOV']


# -----------------------------
# Merge CLV back into dataset
# -----------------------------

df = df.merge(
    clv[['Customer Name','CLV','Orders']],
    on='Customer Name',
    how='left'
)


# -----------------------------
# Save cleaned data
# -----------------------------

os.makedirs('output', exist_ok=True)

df.to_csv(r'c:\Users\PARVATHY\Desktop\projects\p3_KPI+dashboard\output\superstore_cleaned.csv', index=False)
clv.to_csv(r'c:\Users\PARVATHY\Desktop\projects\p3_KPI+dashboard\output\customer_clv.csv', index=False)


# -----------------------------
# Print summary stats
# -----------------------------

print("\nData preparation complete")
print(f"Saved {len(df)} rows to output/superstore_cleaned.csv")
print(f"Unique customers: {clv.shape[0]}")
print(f"Average CLV: ${clv.CLV.mean():.2f}")