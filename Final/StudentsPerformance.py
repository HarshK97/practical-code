# =============================================================================
# STUDENTS PERFORMANCE DATASET - ALL PRACTICALS COMBINED
# Practicals: 2, 12, 35
# Columns: gender, race/ethnicity, parental level of education, lunch,
#          test preparation course, math score, reading score, writing score
# Run from the folder containing StudentsPerformance.csv
# =============================================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, StandardScaler, LabelEncoder
import warnings
warnings.filterwarnings('ignore')

# ── LOAD DATA ─────────────────────────────────────────────────────────────────
df = pd.read_csv('StudentsPerformance.csv')

# Rename columns for easier access
df.columns = ['gender', 'race_ethnicity', 'parental_education', 'lunch',
              'test_prep', 'math_score', 'reading_score', 'writing_score']

print("Dataset loaded. Shape:", df.shape)
print(df.head())
print("\nData Types:\n", df.dtypes)
print("\nMissing Values:\n", df.isnull().sum())
print("\nBasic Statistics:\n", df.describe())


# =============================================================================
# PRACTICAL 2 – BASIC DATA OPERATIONS
# Subset | Merge | Sort | Transpose | Reshape
# =============================================================================
print("\n" + "="*60)
print("PRACTICAL 2 – BASIC DATA OPERATIONS")
print("="*60)

# a) Subset
print("\na) Subsets:")
subset1 = df[df['math_score'] >= 80]
print("  Math score >= 80:", len(subset1))

subset2 = df[df['gender'] == 'female']
print("  Female students:", len(subset2))

subset3 = df[(df['test_prep'] == 'completed') & (df['math_score'] > 70)]
print("  Completed prep + math>70:", len(subset3))

subset4 = df[['gender', 'math_score', 'reading_score', 'writing_score']]
print("\n  Score columns subset:")
print(subset4.head())

# b) Merge
print("\nb) Merge:")
df1 = df.iloc[:500].copy()
df2 = df.iloc[500:].copy()
df_concat = pd.concat([df1, df2], ignore_index=True)
print("  Concat (500+500):", df_concat.shape)

prep_info = pd.DataFrame({
    'test_prep': ['none', 'completed'],
    'prep_duration': ['0 weeks', '8 weeks']
})
df_merged = pd.merge(df, prep_info, on='test_prep')
print("  Merged with prep_info:", df_merged.shape)
print(df_merged[['gender','test_prep','prep_duration','math_score']].head())

# c) Sort
print("\nc) Sort:")
print("  Top 5 by math_score:")
print(df.sort_values('math_score', ascending=False)[['gender','math_score','reading_score','writing_score']].head())

print("\n  Bottom 5 by writing_score:")
print(df.sort_values('writing_score')[['gender','writing_score']].head())

# d) Transpose
print("\nd) Transpose:")
sample = df.head(5)
print("  Original:", sample.shape, "-> Transposed:", sample.T.shape)
print(sample.T)

# e) Reshape
print("\ne) Reshape:")
score_cols = ['math_score', 'reading_score', 'writing_score']
df_melt = df[['gender'] + score_cols].head(10).reset_index()
df_melt = pd.melt(df_melt, id_vars=['index', 'gender'],
                  value_vars=score_cols, var_name='Subject', value_name='Score')
print("  Melted shape:", df_melt.shape)
print(df_melt.head(8))

df_pivot = df_melt.pivot_table(index='gender', columns='Subject', values='Score', aggfunc='mean')
print("\n  Pivot (mean scores by gender):")
print(df_pivot.round(2))


# =============================================================================
# PRACTICAL 12 – DATA CLEANING & ENCODING
# =============================================================================
print("\n" + "="*60)
print("PRACTICAL 12 – DATA CLEANING & ENCODING")
print("="*60)

df12 = df.copy()

# Missing values
print("Missing Values:\n", df12.isnull().sum())
for col in df12.select_dtypes(include=[np.number]).columns:
    df12[col] = df12[col].fillna(df12[col].median())
for col in df12.select_dtypes(include='object').columns:
    df12[col] = df12[col].fillna(df12[col].mode()[0])
print("Missing after fill:", df12.isnull().sum().sum())

# Duplicates
print("Duplicates:", df12.duplicated().sum())

# Outlier detection (IQR)
print("\nOutlier Detection (IQR):")
for col in ['math_score', 'reading_score', 'writing_score']:
    Q1, Q3 = df12[col].quantile(0.25), df12[col].quantile(0.75)
    IQR = Q3 - Q1
    n = ((df12[col] < Q1-1.5*IQR) | (df12[col] > Q3+1.5*IQR)).sum()
    print(f"  {col}: {n} outliers")

# Label Encoding
le = LabelEncoder()
cat_cols = ['gender', 'race_ethnicity', 'parental_education', 'lunch', 'test_prep']
for col in cat_cols:
    df12[col + '_enc'] = le.fit_transform(df12[col])
print("\nLabel Encoded columns added:")
print(df12[['gender','gender_enc','lunch','lunch_enc','test_prep','test_prep_enc']].head())

# One-Hot Encoding
df_ohe = pd.get_dummies(df12[['gender', 'lunch', 'test_prep']], prefix=['gender','lunch','prep'])
print("\nOne-Hot Encoding sample columns:", df_ohe.columns.tolist())
print(df_ohe.head())

# Normalization
num_cols = ['math_score', 'reading_score', 'writing_score']
df12_mm = (df12[num_cols] - df12[num_cols].min()) / (df12[num_cols].max() - df12[num_cols].min())
print("\nMin-Max Normalized scores:")
print(df12_mm.head())

# Groupby
print("\nAverage scores by gender:")
print(df.groupby('gender')[num_cols].mean().round(2))
print("\nAverage scores by test_prep:")
print(df.groupby('test_prep')[num_cols].mean().round(2))


# =============================================================================
# PRACTICAL 35 – VISUALIZATION
# =============================================================================
print("\n" + "="*60)
print("PRACTICAL 35 – VISUALIZATION")
print("="*60)

# --- Histograms ---
plt.figure(figsize=(12, 4))
for i, col in enumerate(['math_score', 'reading_score', 'writing_score']):
    plt.subplot(1, 3, i+1)
    plt.hist(df[col], bins=20, color='steelblue', edgecolor='white')
    plt.xlabel(col.replace('_', ' ').title())
    plt.ylabel('Frequency')
    plt.title(col.replace('_', ' ').title())
plt.tight_layout()
plt.show()

# --- Bar: avg scores by gender ---
gender_means = df.groupby('gender')[['math_score', 'reading_score', 'writing_score']].mean()
x = range(len(gender_means))
width = 0.25

plt.figure(figsize=(8, 5))
for i, col in enumerate(['math_score', 'reading_score', 'writing_score']):
    plt.bar([xi + i*width for xi in x], gender_means[col], width=width, label=col.replace('_score',''))
plt.xticks([xi + width for xi in x], gender_means.index)
plt.ylabel('Average Score')
plt.title('Average Scores by Gender')
plt.legend()
plt.tight_layout()
plt.show()

# --- Bar: avg scores by test_prep ---
prep_means = df.groupby('test_prep')[['math_score', 'reading_score', 'writing_score']].mean()
x = range(len(prep_means))

plt.figure(figsize=(8, 5))
for i, col in enumerate(['math_score', 'reading_score', 'writing_score']):
    plt.bar([xi + i*width for xi in x], prep_means[col], width=width, label=col.replace('_score',''))
plt.xticks([xi + width for xi in x], prep_means.index)
plt.ylabel('Average Score')
plt.title('Average Scores by Test Preparation')
plt.legend()
plt.tight_layout()
plt.show()

# --- Scatter: math vs reading ---
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
colors = df['gender'].map({'male': 'steelblue', 'female': 'coral'})
plt.scatter(df['math_score'], df['reading_score'], c=colors, alpha=0.5, s=20)
plt.xlabel('Math Score')
plt.ylabel('Reading Score')
plt.title('Math vs Reading Score')

plt.subplot(1, 2, 2)
plt.scatter(df['math_score'], df['writing_score'], c=colors, alpha=0.5, s=20)
plt.xlabel('Math Score')
plt.ylabel('Writing Score')
plt.title('Math vs Writing Score')
plt.tight_layout()
plt.show()

print("\n" + "="*60)
print("ALL STUDENTS PRACTICALS DONE")
print("="*60)
