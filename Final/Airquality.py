# =============================================================================
# AIRQUALITY DATASET - ALL PRACTICALS COMBINED
# Practicals: 16, 17
# Columns: Ozone, Solar.R, Wind, Temp, Month, Day
# Run from the folder containing airquality.csv
# =============================================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, StandardScaler
import warnings
warnings.filterwarnings('ignore')

# ── LOAD DATA ─────────────────────────────────────────────────────────────────
df = pd.read_csv('airquality.csv')

print("Dataset loaded. Shape:", df.shape)
print(df.head())
print("\nData Types:\n", df.dtypes)
print("\nMissing Values:\n", df.isnull().sum())
print("\nBasic Statistics:\n", df.describe())


# =============================================================================
# PRACTICAL 16 – SUBSETS & MERGE
# =============================================================================
print("\n" + "="*60)
print("PRACTICAL 16 – SUBSETS & MERGE")
print("="*60)

# a) Subset
print("\na) Subsets:")
high_ozone = df[df['Ozone'] > 50]
print("  Ozone > 50:", len(high_ozone))

high_temp = df[df['Temp'] > 80]
print("  Temp > 80:", len(high_temp))

summer = df[df['Month'].isin([6, 7, 8])]
print("  Summer months (6,7,8):", len(summer))

hot_ozone = df[(df['Temp'] > 80) & (df['Ozone'] > 40)]
print("  Temp>80 & Ozone>40:", len(hot_ozone))

print("\nColumn subset (Ozone, Temp, Month):")
print(df[['Ozone', 'Temp', 'Month']].head())

# b) Merge
print("\nb) Merge:")
may_june = df[df['Month'] == 5].copy()
july_aug  = df[df['Month'].isin([7, 8])].copy()
df_concat = pd.concat([may_june, july_aug], ignore_index=True)
print("  May concat Jul+Aug:", df_concat.shape)

month_labels = pd.DataFrame({
    'Month':     [5, 6, 7, 8, 9],
    'MonthName': ['May','June','July','August','September']
})
df_merged = pd.merge(df, month_labels, on='Month', how='left')
print("  Merged with month names:", df_merged.shape)
print(df_merged[['Month', 'MonthName', 'Ozone', 'Temp']].head())

# c) Sort
print("\nc) Sort:")
print("  Top 5 by Ozone:")
print(df.sort_values('Ozone', ascending=False)[['Ozone','Temp','Month','Day']].head())
print("\n  Lowest 5 Wind:")
print(df.sort_values('Wind')[['Wind','Temp','Month','Day']].head())

# d) Transpose
print("\nd) Transpose:", df.head(5).shape, "->", df.head(5).T.shape)
print(df.head(5).T)

# --- Groupby ---
print("\nGroupby Month (mean):")
print(df.groupby('Month')[['Ozone','Solar.R','Wind','Temp']].mean().round(2))


# =============================================================================
# PRACTICAL 17 – NORMALIZATION & VISUALIZATION
# =============================================================================
print("\n" + "="*60)
print("PRACTICAL 17 – NORMALIZATION & VISUALIZATION")
print("="*60)

df17 = df.copy()

# --- Missing values ---
print("Missing Values:\n", df17.isnull().sum())
df17['Ozone']   = df17['Ozone'].fillna(df17['Ozone'].median())
df17['Solar.R'] = df17['Solar.R'].fillna(df17['Solar.R'].median())
print("Missing after fill:", df17.isnull().sum().sum())

num_cols = ['Ozone', 'Solar.R', 'Wind', 'Temp']

# --- Min-Max Normalization ---
df_mm = (df17[num_cols] - df17[num_cols].min()) / (df17[num_cols].max() - df17[num_cols].min())
print("\nMin-Max Normalized:")
print(df_mm.head())
print(df_mm.describe().round(4))

# --- Z-Score ---
df_zs = (df17[num_cols] - df17[num_cols].mean()) / df17[num_cols].std()
print("\nZ-Score Standardized:")
print(df_zs.describe().round(4))

# --- Decimal Scaling ---
df_dec = df17[num_cols].copy()
print("\nDecimal Scaling divisors:")
for col in num_cols:
    j = int(np.ceil(np.log10(df17[col].abs().max() + 1)))
    df_dec[col] = df17[col] / (10 ** j)
    print(f"  {col}: 10^{j}")
print("After Decimal Scaling:")
print(df_dec.head())

# --- Visualization ---
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.hist(df17['Ozone'].dropna(), bins=20, color='steelblue', edgecolor='white')
plt.xlabel('Ozone')
plt.ylabel('Frequency')
plt.title('Ozone Distribution')

plt.subplot(1, 3, 2)
plt.scatter(df17['Temp'], df17['Ozone'], alpha=0.6, color='coral', s=30)
plt.xlabel('Temperature')
plt.ylabel('Ozone')
plt.title('Temp vs Ozone')

plt.subplot(1, 3, 3)
month_ozone = df17.groupby('Month')['Ozone'].mean()
plt.bar(month_ozone.index, month_ozone.values, color='seagreen')
plt.xlabel('Month')
plt.ylabel('Avg Ozone')
plt.title('Avg Ozone by Month')

plt.tight_layout()
plt.show()

# Line plot: Ozone trend over Days
plt.figure(figsize=(10, 4))
plt.plot(df17.index, df17['Ozone'], color='steelblue', linewidth=1, label='Ozone')
plt.plot(df17.index, df17['Temp'],  color='coral',     linewidth=1, label='Temp')
plt.xlabel('Day index')
plt.ylabel('Value')
plt.title('Ozone & Temperature Over Time')
plt.legend()
plt.tight_layout()
plt.show()

print("\n" + "="*60)
print("ALL AIRQUALITY PRACTICALS DONE")
print("="*60)
