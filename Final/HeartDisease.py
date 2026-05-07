# =============================================================================
# HEART DISEASE DATASET - ALL PRACTICALS COMBINED
# Practical: 13
# Columns: age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang,
#          oldpeak, slope, ca, thal, target
# Run from the folder containing HeartDisease.csv
# =============================================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, StandardScaler, LabelEncoder
import warnings
warnings.filterwarnings('ignore')

# ── LOAD DATA ─────────────────────────────────────────────────────────────────
df = pd.read_csv('HeartDisease.csv')

print("Dataset loaded. Shape:", df.shape)
print(df.head())
print("\nData Types:\n", df.dtypes)
print("\nMissing Values:\n", df.isnull().sum())
print("\nBasic Statistics:\n", df.describe())


# =============================================================================
# PRACTICAL 13 – DATA PREPARATION, CLEANING & ANALYSIS
# =============================================================================
print("\n" + "="*60)
print("PRACTICAL 13 – HEART DISEASE DATA PREPARATION")
print("="*60)

df13 = df.copy()

# --- Missing values ---
print("Missing Values:\n", df13.isnull().sum())
for col in df13.select_dtypes(include=[np.number]).columns:
    df13[col] = df13[col].fillna(df13[col].median())
print("Missing after fill:", df13.isnull().sum().sum())

# --- Duplicates ---
print("Duplicates:", df13.duplicated().sum())
df13 = df13.drop_duplicates()
print("Shape after dedup:", df13.shape)

# --- Outlier Detection ---
print("\nOutlier Detection (IQR):")
for col in ['age', 'trestbps', 'chol', 'thalach']:
    Q1, Q3 = df13[col].quantile(0.25), df13[col].quantile(0.75)
    IQR = Q3 - Q1
    n = ((df13[col] < Q1-1.5*IQR) | (df13[col] > Q3+1.5*IQR)).sum()
    print(f"  {col}: {n} outliers  (Q1={Q1:.1f}, Q3={Q3:.1f})")

# --- Subset / Filter ---
print("\nSubsets:")
heart_pos = df13[df13['target'] == 1]
heart_neg = df13[df13['target'] == 0]
print("  With heart disease (target=1):", len(heart_pos))
print("  Without heart disease (target=0):", len(heart_neg))

high_chol = df13[df13['chol'] > 250]
print("  High cholesterol (>250):", len(high_chol))

# --- Sort ---
print("\nTop 5 by cholesterol:")
print(df13.sort_values('chol', ascending=False)[['age','sex','chol','target']].head())

# --- Groupby Analysis ---
print("\nAvg values by target:")
print(df13.groupby('target')[['age','trestbps','chol','thalach']].mean().round(2))

print("\nAvg values by sex:")
print(df13.groupby('sex')[['age','chol','thalach','target']].mean().round(2))

# --- Feature Engineering ---
df13['age_group'] = pd.cut(df13['age'], bins=[0,40,55,70,100],
                            labels=['Young','Middle','Senior','Old'])
df13['chol_risk'] = df13['chol'].apply(lambda x: 'High' if x > 240 else ('Borderline' if x > 200 else 'Normal'))
print("\nAge group distribution:")
print(df13['age_group'].value_counts())
print("\nCholesterol risk distribution:")
print(df13['chol_risk'].value_counts())

# --- Normalization ---
num_cols = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']

# Min-Max
df_mm = (df13[num_cols] - df13[num_cols].min()) / (df13[num_cols].max() - df13[num_cols].min())
print("\nMin-Max Normalized:")
print(df_mm.head())

# Z-Score
df_zs = (df13[num_cols] - df13[num_cols].mean()) / df13[num_cols].std()
print("\nZ-Score:")
print(df_zs.describe().round(4))

# --- Visualization ---
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
target_counts = df13['target'].value_counts().sort_index()
plt.bar(['No Disease', 'Disease'], target_counts.values, color=['steelblue', 'coral'])
plt.ylabel('Count')
plt.title('Heart Disease Count')

plt.subplot(1, 3, 2)
plt.hist(df13['age'], bins=15, color='seagreen', edgecolor='white')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Age Distribution')

plt.subplot(1, 3, 3)
plt.scatter(df13['age'], df13['chol'], c=df13['target'], cmap='coolwarm', alpha=0.7, s=40)
plt.xlabel('Age')
plt.ylabel('Cholesterol')
plt.title('Age vs Cholesterol (by Target)')
plt.colorbar(label='Target')

plt.tight_layout()
plt.show()

# Bar: avg cholesterol by age group
plt.figure(figsize=(8, 4))
chol_by_age = df13.groupby('age_group', observed=True)['chol'].mean()
plt.bar(chol_by_age.index, chol_by_age.values, color='mediumpurple')
plt.xlabel('Age Group')
plt.ylabel('Avg Cholesterol')
plt.title('Average Cholesterol by Age Group')
plt.tight_layout()
plt.show()

print("\n" + "="*60)
print("ALL HEART DISEASE PRACTICALS DONE")
print("="*60)
