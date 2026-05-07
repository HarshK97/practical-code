# =============================================================================
# SALARIES DATASET - ALL PRACTICALS COMBINED
# Practicals: 28, 29
# Columns: rank, discipline, phd, service, sex, salary
# Run from the folder containing Salaries.csv
# =============================================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
import warnings
warnings.filterwarnings('ignore')

# ── LOAD DATA ─────────────────────────────────────────────────────────────────
df = pd.read_csv('Salaries.csv')

print("Dataset loaded. Shape:", df.shape)
print(df.head())
print("\nData Types:\n", df.dtypes)
print("\nMissing Values:\n", df.isnull().sum())
print("\nBasic Statistics:\n", df.describe())


# =============================================================================
# PRACTICAL 28 – BASIC DATA OPERATIONS
# Subset | Merge | Sort | Transpose | Reshape
# =============================================================================
print("\n" + "="*60)
print("PRACTICAL 28 – BASIC DATA OPERATIONS")
print("="*60)

# a) Subset
print("\na) Subsets:")
profs  = df[df['rank'] == 'Prof']
assoc  = df[df['rank'] == 'AssocProf']
asst   = df[df['rank'] == 'AsstProf']
print("  Professors:", len(profs), "| AssocProf:", len(assoc), "| AsstProf:", len(asst))

high_salary = df[df['salary'] > 150000]
print("  Salary > 150000:", len(high_salary))

experienced = df[df['service'] > 20]
print("  Service > 20 years:", len(experienced))

subset_cols = df[['rank', 'sex', 'salary', 'phd', 'service']]
print("\n  Column subset:")
print(subset_cols.head())

# b) Merge / Concat
print("\nb) Merge:")
df1 = df.iloc[:40].copy()
df2 = df.iloc[40:].copy()
df_concat = pd.concat([df1, df2], ignore_index=True)
print("  Concat:", df1.shape, "+", df2.shape, "=", df_concat.shape)

rank_info = pd.DataFrame({
    'rank': ['Prof', 'AssocProf', 'AsstProf'],
    'rank_level': [3, 2, 1]
})
df_merged = pd.merge(df, rank_info, on='rank', how='left')
print("  Merged with rank_level:")
print(df_merged[['rank','rank_level','salary']].head())

# c) Sort
print("\nc) Sort:")
print("  Top 5 salaries:")
print(df.sort_values('salary', ascending=False)[['rank','sex','salary','service']].head())
print("\n  Sort by rank ASC, salary DESC:")
print(df.sort_values(['rank','salary'], ascending=[True,False])[['rank','salary','sex']].head(6))

# d) Transpose
print("\nd) Transpose:", df.head(5).shape, "->", df.head(5).T.shape)
print(df.head(5).T)

# e) Reshape
print("\ne) Reshape (melt):")
df_melt = df[['rank','salary','phd']].head(5).reset_index()
df_melt = pd.melt(df_melt, id_vars=['index','rank'], value_vars=['salary','phd'],
                  var_name='Metric', value_name='Value')
print(df_melt)

print("\nGroupby rank:")
print(df.groupby('rank')[['salary','phd','service']].mean().round(2))


# =============================================================================
# PRACTICAL 29 – FILTERING, ENCODING & VISUALIZATION
# =============================================================================
print("\n" + "="*60)
print("PRACTICAL 29 – FILTERING, ENCODING & VISUALIZATION")
print("="*60)

# --- Filtering queries ---
print("\n--- Filtering ---")
# Male Professors with salary > 120000
male_profs = df[(df['rank'] == 'Prof') & (df['sex'] == 'Male') & (df['salary'] > 120000)]
print("Male Professors salary>120k:", len(male_profs))
print(male_profs[['rank','sex','salary','service']].head())

# Discipline A with phd > 10
disc_a = df[(df['discipline'] == 'A') & (df['phd'] > 10)]
print("\nDiscipline A & phd>10:", len(disc_a))

# isin filter
print("\nisin filter (Prof or AsstProf):")
print(df[df['rank'].isin(['Prof','AsstProf'])][['rank','salary']].describe())

# --- Cleaning & Encoding ---
print("\n--- Encoding ---")
df29 = df.copy()
le = LabelEncoder()
df29['rank_enc']       = le.fit_transform(df29['rank'])
df29['sex_enc']        = LabelEncoder().fit_transform(df29['sex'])
df29['discipline_enc'] = LabelEncoder().fit_transform(df29['discipline'])
print("rank encoding:", dict(zip(le.classes_, le.transform(le.classes_))))

# One-Hot
df_ohe = pd.get_dummies(df29['rank'], prefix='rank')
df29 = pd.concat([df29, df_ohe], axis=1)
print("\nAfter One-Hot (rank):")
print(df29[['rank','rank_AsstProf','rank_AssocProf','rank_Prof']].head())

# --- Min-Max Normalization ---
num_cols = ['salary', 'phd', 'service']
df_mm = (df29[num_cols] - df29[num_cols].min()) / (df29[num_cols].max() - df29[num_cols].min())
print("\nMin-Max Normalized:")
print(df_mm.describe().round(4))

# --- Groupby analysis ---
print("\nAvg salary by rank and sex:")
print(df.groupby(['rank','sex'])['salary'].mean().round(0))

# --- Visualization ---
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
rank_avg = df.groupby('rank')['salary'].mean().sort_values(ascending=False)
plt.bar(rank_avg.index, rank_avg.values, color=['steelblue','coral','seagreen'])
plt.ylabel('Avg Salary')
plt.title('Avg Salary by Rank')

plt.subplot(1, 3, 2)
sex_avg = df.groupby('sex')['salary'].mean()
plt.bar(sex_avg.index, sex_avg.values, color=['mediumpurple','goldenrod'])
plt.ylabel('Avg Salary')
plt.title('Avg Salary by Sex')

plt.subplot(1, 3, 3)
plt.scatter(df['service'], df['salary'], alpha=0.6, color='steelblue', s=30)
plt.xlabel('Years of Service')
plt.ylabel('Salary')
plt.title('Service vs Salary')

plt.tight_layout()
plt.show()

# Histogram: salary distribution
plt.figure(figsize=(8, 4))
plt.hist(df['salary'], bins=20, color='coral', edgecolor='white')
plt.xlabel('Salary')
plt.ylabel('Frequency')
plt.title('Salary Distribution')
plt.tight_layout()
plt.show()

print("\n" + "="*60)
print("ALL SALARIES PRACTICALS DONE")
print("="*60)
