# =============================================================================
# IRIS DATASET - ALL PRACTICALS COMBINED
# Practicals: 1, 14, 40
# Columns: Id, SepalLengthCm, SepalWidthCm, PetalLengthCm, PetalWidthCm, Species
# Run from the folder containing Iris.csv
# =============================================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, StandardScaler, LabelEncoder
import warnings
warnings.filterwarnings('ignore')

# ── LOAD DATA ─────────────────────────────────────────────────────────────────
df = pd.read_csv('Iris.csv')
if 'Id' in df.columns:
    df = df.drop(columns=['Id'])

print("Dataset loaded. Shape:", df.shape)
print(df.head())
print("\nData Types:\n", df.dtypes)
print("\nMissing Values:\n", df.isnull().sum())
print("\nBasic Statistics:\n", df.describe())


# =============================================================================
# PRACTICAL 1 – BASIC DATA OPERATIONS
# Subset | Merge | Sort | Transpose | Reshape
# =============================================================================
print("\n" + "="*60)
print("PRACTICAL 1 – BASIC DATA OPERATIONS")
print("="*60)

# a) Subset
print("\na) Subsets:")
subset1 = df[df['PetalLengthCm'] > 1.5]
print("  PetalLength > 1.5:", len(subset1), "rows")

subset2 = df[df['Species'] == 'Iris-setosa']
print("  Setosa only:", len(subset2), "rows")

subset3 = df[(df['PetalLengthCm'] > 1.5) & (df['Species'] == 'Iris-setosa')]
print("  PetalLength>1.5 AND Setosa:", len(subset3), "rows")
print(subset3.head())

subset4 = df[['SepalLengthCm', 'SepalWidthCm', 'Species']]
print("\n  Column subset (Sepal cols + Species):")
print(subset4.head())

# b) Merge
print("\nb) Merge:")
species_info = pd.DataFrame({
    'Species':  ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica'],
    'Color':    ['purple', 'blue', 'pink'],
    'Habitat':  ['temperate', 'temperate', 'temperate']
})
df_merged = pd.merge(df, species_info, on='Species')
print("  Merged with species_info:", df_merged.shape)
print(df_merged.head())

df1 = df.iloc[:75].copy()
df2 = df.iloc[75:].copy()
df_concat = pd.concat([df1, df2], ignore_index=True)
print("  Concat (75+75):", df_concat.shape)

# c) Sort
print("\nc) Sort:")
df_sorted = df.sort_values(['SepalWidthCm', 'SepalLengthCm'])
print("  Sorted by SepalWidth then SepalLength:")
print(df_sorted[['SepalLengthCm', 'SepalWidthCm', 'Species']].head())

df_sorted2 = df.sort_values('PetalLengthCm', ascending=False)
print("  Top 5 by PetalLength:")
print(df_sorted2[['PetalLengthCm', 'Species']].head())

# d) Transpose
print("\nd) Transpose:")
sample = df.head(5)
print("  Original:", sample.shape, "-> Transposed:", sample.T.shape)
print(sample.T)

# e) Reshape – melt and pivot
print("\ne) Reshape:")
df_melt = df.head(10).melt(id_vars='Species',
                            value_vars=['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm'],
                            var_name='Measurement', value_name='Value')
print("  Melted shape:", df_melt.shape)
print(df_melt.head(8))

df_pivot = df_melt.pivot_table(index='Species', columns='Measurement', values='Value', aggfunc='mean')
print("\n  Pivot (mean by species):")
print(df_pivot.round(2))


# =============================================================================
# PRACTICAL 14 – DATA CLEANING & ADVANCED OPERATIONS
# =============================================================================
print("\n" + "="*60)
print("PRACTICAL 14 – DATA CLEANING & ADVANCED OPERATIONS")
print("="*60)

df14 = df.copy()

# Missing values
print("\nMissing Values:\n", df14.isnull().sum())
df14 = df14.fillna(df14.median(numeric_only=True))
print("Missing after fill:", df14.isnull().sum().sum())

# Duplicates
print("Duplicates:", df14.duplicated().sum())
df14 = df14.drop_duplicates()
print("Shape after dedup:", df14.shape)

# Label Encoding
le = LabelEncoder()
df14['Species_encoded'] = le.fit_transform(df14['Species'])
print("\nSpecies encoding:", dict(zip(le.classes_, le.transform(le.classes_))))

# One-Hot Encoding
df_ohe = pd.get_dummies(df14['Species'], prefix='Sp')
df14 = pd.concat([df14, df_ohe], axis=1)
print("\nAfter One-Hot Encoding, columns:", df14.columns.tolist())
print(df14[['Species', 'Species_encoded', 'Sp_Iris-setosa', 'Sp_Iris-versicolor', 'Sp_Iris-virginica']].head())

# Min-Max Normalization
num_cols = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']
df14_mm = (df14[num_cols] - df14[num_cols].min()) / (df14[num_cols].max() - df14[num_cols].min())
print("\nMin-Max Normalized:")
print(df14_mm.describe().round(4))

# Z-Score
df14_zs = (df14[num_cols] - df14[num_cols].mean()) / df14[num_cols].std()
print("\nZ-Score Standardized:")
print(df14_zs.describe().round(4))

# Outlier detection (IQR)
print("\nOutlier Detection (IQR):")
for col in num_cols:
    Q1, Q3 = df14[col].quantile(0.25), df14[col].quantile(0.75)
    IQR = Q3 - Q1
    n = ((df14[col] < Q1-1.5*IQR) | (df14[col] > Q3+1.5*IQR)).sum()
    print(f"  {col}: {n} outliers")

# Groupby
print("\nGroup by Species:")
print(df.groupby('Species')[num_cols].mean().round(2))


# =============================================================================
# PRACTICAL 40 – VISUALIZATION
# =============================================================================
print("\n" + "="*60)
print("PRACTICAL 40 – VISUALIZATION")
print("="*60)

colors_map = {'Iris-setosa': 'blue', 'Iris-versicolor': 'orange', 'Iris-virginica': 'green'}
colors = df['Species'].map(colors_map)

# --- Scatter plots ---
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
for sp, grp in df.groupby('Species'):
    plt.scatter(grp['SepalLengthCm'], grp['SepalWidthCm'], label=sp, alpha=0.7, s=30)
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.title('Sepal Length vs Width')
plt.legend(fontsize=7)

plt.subplot(1, 3, 2)
for sp, grp in df.groupby('Species'):
    plt.scatter(grp['PetalLengthCm'], grp['PetalWidthCm'], label=sp, alpha=0.7, s=30)
plt.xlabel('Petal Length')
plt.ylabel('Petal Width')
plt.title('Petal Length vs Width')
plt.legend(fontsize=7)

plt.subplot(1, 3, 3)
for sp, grp in df.groupby('Species'):
    plt.scatter(grp['SepalLengthCm'], grp['PetalLengthCm'], label=sp, alpha=0.7, s=30)
plt.xlabel('Sepal Length')
plt.ylabel('Petal Length')
plt.title('Sepal vs Petal Length')
plt.legend(fontsize=7)

plt.tight_layout()
plt.show()

# --- Histograms ---
plt.figure(figsize=(12, 4))
for i, col in enumerate(num_cols):
    plt.subplot(1, 4, i+1)
    plt.hist(df[col], bins=20, color='steelblue', edgecolor='white')
    plt.xlabel(col)
    plt.ylabel('Frequency')
    plt.title(col)
plt.tight_layout()
plt.show()

# --- Bar chart: mean by species ---
means = df.groupby('Species')[num_cols].mean()
x = range(len(means))
width = 0.2

plt.figure(figsize=(10, 5))
for i, col in enumerate(num_cols):
    plt.bar([xi + i*width for xi in x], means[col], width=width, label=col)
plt.xticks([xi + width*1.5 for xi in x], means.index, rotation=10)
plt.ylabel('Mean Value')
plt.title('Mean Measurements by Species')
plt.legend()
plt.tight_layout()
plt.show()

print("\n" + "="*60)
print("ALL IRIS PRACTICALS DONE")
print("="*60)
