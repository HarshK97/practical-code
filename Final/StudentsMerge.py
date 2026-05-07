# =============================================================================
# STUDENT INFO + SCORES - ALL PRACTICALS COMBINED
# Practicals: 6, 7
# Files: student_info.csv (StudentID,Name,Age,Email,Grade,History)
#        student_scores.csv (StudentID,Math,Science,English)
# Run from the folder containing both CSV files
# =============================================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
import warnings
warnings.filterwarnings('ignore')

# ── LOAD DATA ─────────────────────────────────────────────────────────────────
info   = pd.read_csv('student_info.csv')
scores = pd.read_csv('student_scores.csv')

print("student_info.csv:")
print(info)
print("\nstudent_scores.csv:")
print(scores)


# =============================================================================
# PRACTICAL 6 – DATA CLEANING & MERGE
# =============================================================================
print("\n" + "="*60)
print("PRACTICAL 6 – DATA CLEANING & MERGE")
print("="*60)

# --- Clean student_info ---
print("\n--- Clean student_info ---")
print("Missing:\n", info.isnull().sum())

# Fill History missing with median
info['History'] = info['History'].fillna(info['History'].median())
print("After fill:\n", info)

# Remove duplicate emails
print("Duplicates:", info.duplicated().sum())

# Standardize Email to lowercase
info['Email'] = info['Email'].str.lower().str.strip()

# --- Clean student_scores ---
print("\n--- Clean student_scores ---")
print("Scores before:\n", scores)

# Replace invalid score (-1 means missing data)
scores['Math'] = scores['Math'].replace(-1, np.nan)
scores['Math'] = scores['Math'].fillna(scores['Math'].mean())
print("After cleaning Math score:")
print(scores)

# --- Merge ---
print("\n--- Merge on StudentID ---")
df_merged = pd.merge(info, scores, on='StudentID', how='inner')
print("Inner join result:")
print(df_merged)

df_left = pd.merge(info, scores, on='StudentID', how='left')
print("\nLeft join (all info students):")
print(df_left)

# --- Feature Engineering ---
print("\n--- Feature Engineering ---")
df_merged['Total_Score'] = df_merged['Math'] + df_merged['Science'] + df_merged['English']
df_merged['Avg_Score']   = (df_merged['Total_Score'] / 3).round(2)
print(df_merged[['Name', 'Math', 'Science', 'English', 'Total_Score', 'Avg_Score']])


# =============================================================================
# PRACTICAL 7 – DATA CLEANING & FEATURE ENGINEERING
# =============================================================================
print("\n" + "="*60)
print("PRACTICAL 7 – FEATURE ENGINEERING & ANALYSIS")
print("="*60)

df7 = df_merged.copy()

# --- Sort and filter ---
print("\nTop students by Avg_Score:")
print(df7.sort_values('Avg_Score', ascending=False)[['Name','Grade','Avg_Score']])

print("\nGrade 12 students:")
print(df7[df7['Grade'] == 12][['Name','Avg_Score','Total_Score']])

# --- Performance category ---
def classify(score):
    if score >= 90:   return 'Excellent'
    elif score >= 80: return 'Good'
    elif score >= 70: return 'Average'
    else:             return 'Poor'

df7['Performance'] = df7['Avg_Score'].apply(classify)
print("\nWith Performance label:")
print(df7[['Name', 'Avg_Score', 'Performance']])

# --- Label Encoding ---
le = LabelEncoder()
df7['Grade_encoded'] = le.fit_transform(df7['Grade'].astype(str))
df7['Perf_encoded']  = LabelEncoder().fit_transform(df7['Performance'])
print("\nEncoded columns:")
print(df7[['Name','Grade','Grade_encoded','Performance','Perf_encoded']])

# --- Normalization ---
df7['Math_norm']    = (df7['Math']    - df7['Math'].min())    / (df7['Math'].max()    - df7['Math'].min())
df7['Science_norm'] = (df7['Science'] - df7['Science'].min()) / (df7['Science'].max() - df7['Science'].min())
df7['English_norm'] = (df7['English'] - df7['English'].min()) / (df7['English'].max() - df7['English'].min())
print("\nNormalized scores:")
print(df7[['Name','Math_norm','Science_norm','English_norm']].round(3))

# --- Group by grade ---
print("\nAvg scores by Grade:")
print(df7.groupby('Grade')[['Math','Science','English','Avg_Score']].mean().round(2))

# --- Visualization ---
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.bar(df7['Name'], df7['Avg_Score'], color='steelblue')
plt.xticks(rotation=30, fontsize=8)
plt.ylabel('Avg Score')
plt.title('Average Score per Student')

plt.subplot(1, 3, 2)
subjects = ['Math', 'Science', 'English']
means = [df7[s].mean() for s in subjects]
plt.bar(subjects, means, color=['coral', 'seagreen', 'mediumpurple'])
plt.ylabel('Average Score')
plt.title('Class Average by Subject')

plt.subplot(1, 3, 3)
perf_counts = df7['Performance'].value_counts()
plt.bar(perf_counts.index, perf_counts.values, color='goldenrod')
plt.ylabel('Count')
plt.title('Performance Category Count')

plt.tight_layout()
plt.show()

print("\n" + "="*60)
print("ALL STUDENT PRACTICALS DONE")
print("="*60)
