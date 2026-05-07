# =============================================================================
# APPLICANTS + EXAM SCORES DATASET - ALL PRACTICALS COMBINED
# Practical: 9
# Files: applicants.csv  (ApplicationID, Name, GPA, Admission_Status)
#        exam_scores.csv (ApplicationID, SAT, ACT)
# Run from the folder containing both CSV files
# =============================================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import warnings
warnings.filterwarnings('ignore')

# ── LOAD DATA ─────────────────────────────────────────────────────────────────
applicants  = pd.read_csv('applicants.csv')
exam_scores = pd.read_csv('exam_scores.csv')

print("applicants.csv:")
print(applicants)
print("\nexam_scores.csv:")
print(exam_scores)


# =============================================================================
# PRACTICAL 9 – CLEANING, MERGE & NORMALIZATION
# =============================================================================
print("\n" + "="*60)
print("PRACTICAL 9 – CLEANING, MERGE & NORMALIZATION")
print("="*60)

# --- Clean applicants ---
print("\n--- Clean applicants ---")
print("Missing:\n", applicants.isnull().sum())
applicants['GPA'] = applicants['GPA'].fillna(applicants['GPA'].median())
print("After fill:\n", applicants)

# --- Clean exam_scores ---
print("\n--- Clean exam_scores ---")
print("Missing:\n", exam_scores.isnull().sum())
exam_scores['SAT'] = exam_scores['SAT'].fillna(exam_scores['SAT'].mean())
print("After fill:\n", exam_scores)

# --- Merge ---
print("\n--- Merge ---")
df_inner = pd.merge(applicants, exam_scores, on='ApplicationID', how='inner')
print("Inner join:")
print(df_inner)

df_outer = pd.merge(applicants, exam_scores, on='ApplicationID', how='outer')
print("\nOuter join (all records):")
print(df_outer)

# --- Analysis ---
print("\n--- Analysis ---")
print("Admission Status counts:")
print(df_inner['Admission_Status'].value_counts())

print("\nAvg GPA / SAT / ACT by Admission Status:")
print(df_inner.groupby('Admission_Status')[['GPA','SAT','ACT']].mean().round(2))

# --- Normalization ---
print("\n--- Normalization ---")
num_cols = ['GPA', 'SAT', 'ACT']
df_num = df_inner[num_cols].copy()

# Min-Max
df_mm = (df_num - df_num.min()) / (df_num.max() - df_num.min())
print("Min-Max Normalized:")
print(df_mm.round(4))

# Z-Score
df_zs = (df_num - df_num.mean()) / df_num.std()
print("\nZ-Score:")
print(df_zs.round(4))

# --- Sort & filter ---
print("\nSorted by GPA (desc):")
print(df_inner.sort_values('GPA', ascending=False)[['Name','GPA','SAT','Admission_Status']])

admitted = df_inner[df_inner['Admission_Status'] == 'Admitted']
print("\nAdmitted students:")
print(admitted[['Name','GPA','SAT','ACT']])

# --- Visualization ---
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
status_counts = df_inner['Admission_Status'].value_counts()
plt.bar(status_counts.index, status_counts.values, color=['steelblue','coral'])
plt.ylabel('Count')
plt.title('Admission Status Count')

plt.subplot(1, 2, 2)
colors = df_inner['Admission_Status'].map({'Admitted':'steelblue','Rejected':'coral'})
plt.scatter(df_inner['GPA'], df_inner['SAT'], c=colors, s=100)
plt.xlabel('GPA')
plt.ylabel('SAT Score')
plt.title('GPA vs SAT (by Status)')

plt.tight_layout()
plt.show()

print("\n" + "="*60)
print("ALL APPLICANTS PRACTICALS DONE")
print("="*60)
