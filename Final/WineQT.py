# =============================================================================
# WINE QUALITY DATASET - ALL PRACTICALS COMBINED
# Practical: 4
# Columns: fixed acidity, volatile acidity, citric acid, residual sugar,
#          chlorides, free sulfur dioxide, total sulfur dioxide, density,
#          pH, sulphates, alcohol, quality, Id
# Run from the folder containing WineQT.csv
# =============================================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, StandardScaler
import warnings
warnings.filterwarnings('ignore')

# ── LOAD DATA ─────────────────────────────────────────────────────────────────
df = pd.read_csv('WineQT.csv')
if 'Id' in df.columns:
    df = df.drop(columns=['Id'])

print("Dataset loaded. Shape:", df.shape)
print(df.head())
print("\nData Types:\n", df.dtypes)
print("\nMissing Values:\n", df.isnull().sum())
print("\nBasic Statistics:\n", df.describe())


# =============================================================================
# PRACTICAL 4 – DATA OPERATIONS, CLEANING & VISUALIZATION
# =============================================================================
print("\n" + "="*60)
print("PRACTICAL 4 – DATA OPERATIONS (Wine Quality)")
print("="*60)

# a) Subset
print("\na) Subsets:")
high_quality = df[df['quality'] >= 7]
low_quality  = df[df['quality'] <= 4]
print("  High quality (>=7):", len(high_quality))
print("  Low quality (<=4):", len(low_quality))

high_alcohol = df[df['alcohol'] > 11]
print("  Alcohol > 11:", len(high_alcohol))

subset_cols = df[['fixed acidity', 'alcohol', 'quality']]
print("\n  Column subset (acidity, alcohol, quality):")
print(subset_cols.head())

# b) Merge / Concat
print("\nb) Merge:")
df1 = df.iloc[:500].copy()
df2 = df.iloc[500:].copy()
df_concat = pd.concat([df1, df2], ignore_index=True)
print("  Concat:", df1.shape, "+", df2.shape, "=", df_concat.shape)

quality_label = pd.DataFrame({'quality': range(3, 9),
                               'quality_label': ['Poor','Poor','Average','Average','Good','Excellent']})
df_merged = pd.merge(df, quality_label, on='quality', how='left')
print("  Merged with quality labels:", df_merged.shape)
print(df_merged[['quality', 'quality_label', 'alcohol']].value_counts().head())

# c) Sort
print("\nc) Sort:")
print("  Top 5 by alcohol:")
print(df.sort_values('alcohol', ascending=False)[['alcohol', 'quality', 'pH']].head())

print("\n  Sort by quality DESC then alcohol DESC:")
print(df.sort_values(['quality','alcohol'], ascending=[False,False])[['quality','alcohol']].head(6))

# d) Transpose
print("\nd) Transpose:", df.head(5).shape, "->", df.head(5).T.shape)
print(df.head(5).T)

# e) Reshape
print("\ne) Reshape (melt):")
cols3 = ['fixed acidity', 'volatile acidity', 'alcohol']
df_melt = df[cols3].head(6).reset_index()
df_melt = pd.melt(df_melt, id_vars='index', value_vars=cols3, var_name='Feature', value_name='Value')
print(df_melt)

print("\nGroupby quality:")
print(df.groupby('quality')[['alcohol', 'pH', 'density']].mean().round(3))


# --- Data Cleaning ---
print("\n" + "="*60)
print("DATA CLEANING")
print("="*60)

df_c = df.copy()
print("Missing:", df_c.isnull().sum().sum())
df_c = df_c.fillna(df_c.median(numeric_only=True))
print("Duplicates:", df_c.duplicated().sum())
df_c = df_c.drop_duplicates()
print("Shape after clean:", df_c.shape)

print("\nOutlier Detection (IQR):")
for col in ['fixed acidity', 'volatile acidity', 'alcohol', 'quality']:
    Q1, Q3 = df_c[col].quantile(0.25), df_c[col].quantile(0.75)
    IQR = Q3 - Q1
    n = ((df_c[col] < Q1-1.5*IQR) | (df_c[col] > Q3+1.5*IQR)).sum()
    print(f"  {col}: {n} outliers")


# --- Normalization ---
print("\n" + "="*60)
print("NORMALIZATION")
print("="*60)

num_cols = df_c.select_dtypes(include=[np.number]).columns.tolist()

# Min-Max
df_mm = (df_c[num_cols] - df_c[num_cols].min()) / (df_c[num_cols].max() - df_c[num_cols].min())
print("Min-Max Normalized (first 3 cols):")
print(df_mm[num_cols[:3]].describe().round(4))

# Z-Score
df_zs = (df_c[num_cols] - df_c[num_cols].mean()) / df_c[num_cols].std()
print("\nZ-Score (first 3 cols):")
print(df_zs[num_cols[:3]].describe().round(4))


# --- Visualization ---
print("\n" + "="*60)
print("VISUALIZATION")
print("="*60)

plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.hist(df['quality'], bins=range(3, 10), color='steelblue', edgecolor='white', align='left')
plt.xlabel('Quality')
plt.ylabel('Count')
plt.title('Quality Distribution')

plt.subplot(1, 3, 2)
plt.scatter(df['alcohol'], df['quality'], alpha=0.4, s=15, color='coral')
plt.xlabel('Alcohol')
plt.ylabel('Quality')
plt.title('Alcohol vs Quality')

plt.subplot(1, 3, 3)
plt.scatter(df['fixed acidity'], df['volatile acidity'], alpha=0.4, s=15, color='seagreen')
plt.xlabel('Fixed Acidity')
plt.ylabel('Volatile Acidity')
plt.title('Fixed vs Volatile Acidity')

plt.tight_layout()
plt.show()

# Bar: avg alcohol by quality
plt.figure(figsize=(8, 4))
avg_alc = df.groupby('quality')['alcohol'].mean()
plt.bar(avg_alc.index, avg_alc.values, color='mediumpurple')
plt.xlabel('Quality')
plt.ylabel('Avg Alcohol')
plt.title('Average Alcohol by Quality')
plt.tight_layout()
plt.show()

print("\n" + "="*60)
print("ALL WINE QUALITY PRACTICALS DONE")
print("="*60)
