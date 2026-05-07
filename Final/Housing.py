# =============================================================================
# HOUSING DATASET - ALL PRACTICALS COMBINED
# Practicals: 3, 36
# Columns: longitude, latitude, housing_median_age, total_rooms,
#          total_bedrooms, population, households, median_income,
#          median_house_value, ocean_proximity
# Run from the folder containing housing.csv
# =============================================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, StandardScaler, LabelEncoder
import warnings
warnings.filterwarnings('ignore')

# ── LOAD DATA ─────────────────────────────────────────────────────────────────
df = pd.read_csv('housing.csv')

print("Dataset loaded. Shape:", df.shape)
print(df.head())
print("\nData Types:\n", df.dtypes)
print("\nMissing Values:\n", df.isnull().sum())
print("\nBasic Statistics:\n", df.describe())


# =============================================================================
# PRACTICAL 3 – BASIC DATA OPERATIONS
# Subset | Merge | Sort | Transpose | Reshape
# =============================================================================
print("\n" + "="*60)
print("PRACTICAL 3 – BASIC DATA OPERATIONS")
print("="*60)

# a) Subset
print("\na) Subsets:")
subset1 = df[df['median_house_value'] > 300000]
print("  median_house_value > 300000:", len(subset1))

subset2 = df[df['ocean_proximity'] == 'NEAR BAY']
print("  NEAR BAY:", len(subset2))

subset3 = df[(df['housing_median_age'] > 30) & (df['median_income'] > 5)]
print("  Age>30 & Income>5:", len(subset3))

subset4 = df[['median_house_value', 'median_income', 'housing_median_age', 'ocean_proximity']]
print("\n  Column subset:")
print(subset4.head())

# b) Merge
print("\nb) Merge:")
df1 = df.iloc[:10000].copy()
df2 = df.iloc[10000:].copy()
df_concat = pd.concat([df1, df2], ignore_index=True)
print("  Concat:", df1.shape, "+", df2.shape, "=", df_concat.shape)

proximity_info = pd.DataFrame({
    'ocean_proximity': ['NEAR BAY', '<1H OCEAN', 'INLAND', 'NEAR OCEAN', 'ISLAND'],
    'coastal': [True, True, False, True, True]
})
df_merged = pd.merge(df, proximity_info, on='ocean_proximity', how='left')
print("  Merged with proximity_info:", df_merged.shape)
print(df_merged[['ocean_proximity', 'coastal', 'median_house_value']].head())

# c) Sort
print("\nc) Sort:")
print("  Top 5 by median_house_value:")
print(df.sort_values('median_house_value', ascending=False)[['median_house_value', 'median_income', 'ocean_proximity']].head())

print("\n  Multi-sort (ocean_proximity ASC, value DESC):")
print(df.sort_values(['ocean_proximity', 'median_house_value'], ascending=[True, False])[
    ['ocean_proximity', 'median_house_value']].head(6))

# d) Transpose
print("\nd) Transpose:")
sample = df.head(5)
print("  Original:", sample.shape, "-> Transposed:", sample.T.shape)
print(sample.T)

# e) Reshape
print("\ne) Reshape (melt):")
cols = ['median_house_value', 'median_income', 'total_rooms']
df_melt = df[cols].head(5).reset_index()
df_melt = pd.melt(df_melt, id_vars='index', value_vars=cols, var_name='Feature', value_name='Value')
print(df_melt)

print("\nGrouped (pivot) by ocean_proximity:")
print(df.groupby('ocean_proximity')[['median_house_value', 'median_income']].mean().round(2))


# =============================================================================
# PRACTICAL 36 – DATA CLEANING, NORMALIZATION & VISUALIZATION
# =============================================================================
print("\n" + "="*60)
print("PRACTICAL 36 – CLEANING, NORMALIZATION & VISUALIZATION")
print("="*60)

df36 = df.copy()

# --- Missing values ---
print("Missing Values:\n", df36.isnull().sum())
df36['total_bedrooms'] = df36['total_bedrooms'].fillna(df36['total_bedrooms'].median())
print("Missing after fill:", df36.isnull().sum().sum())

# --- Outlier detection ---
print("\nOutlier Detection (IQR):")
num_cols = ['median_house_value', 'median_income', 'total_rooms', 'population']
for col in num_cols:
    Q1, Q3 = df36[col].quantile(0.25), df36[col].quantile(0.75)
    IQR = Q3 - Q1
    n = ((df36[col] < Q1-1.5*IQR) | (df36[col] > Q3+1.5*IQR)).sum()
    print(f"  {col}: {n} outliers")

# --- Encoding ---
le = LabelEncoder()
df36['ocean_proximity_enc'] = le.fit_transform(df36['ocean_proximity'])
print("\nOcean proximity encoding:", dict(zip(le.classes_, le.transform(le.classes_))))

# --- Min-Max Normalization ---
scaler = MinMaxScaler()
df36_mm = pd.DataFrame(scaler.fit_transform(df36[num_cols]), columns=num_cols)
print("\nMin-Max Normalized:")
print(df36_mm.describe().round(4))

# --- Z-Score ---
df36_zs = (df36[num_cols] - df36[num_cols].mean()) / df36[num_cols].std()
print("\nZ-Score:")
print(df36_zs.describe().round(4))

# --- Visualizations ---
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.hist(df36['median_house_value'], bins=40, color='steelblue', edgecolor='white')
plt.xlabel('Median House Value')
plt.ylabel('Frequency')
plt.title('House Value Distribution')

plt.subplot(1, 3, 2)
plt.scatter(df36['median_income'], df36['median_house_value'], alpha=0.2, s=5, color='coral')
plt.xlabel('Median Income')
plt.ylabel('Median House Value')
plt.title('Income vs House Value')

plt.subplot(1, 3, 3)
prox_counts = df36['ocean_proximity'].value_counts()
plt.bar(prox_counts.index, prox_counts.values, color='seagreen')
plt.xticks(rotation=20, fontsize=8)
plt.ylabel('Count')
plt.title('Count by Ocean Proximity')

plt.tight_layout()
plt.show()

# Bar: avg house value by proximity
plt.figure(figsize=(8, 5))
avg_val = df.groupby('ocean_proximity')['median_house_value'].mean().sort_values(ascending=False)
plt.bar(avg_val.index, avg_val.values, color='mediumpurple')
plt.xticks(rotation=15, fontsize=9)
plt.ylabel('Avg Median House Value')
plt.title('Avg House Value by Ocean Proximity')
plt.tight_layout()
plt.show()

print("\n" + "="*60)
print("ALL HOUSING PRACTICALS DONE")
print("="*60)
