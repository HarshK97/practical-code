# =============================================================================
# PATIENTS + VISITS DATASET - ALL PRACTICALS COMBINED
# Practical: 8
# Files: patients.csv (PatientID, Name, Age, Gender)
#        visits.csv  (VisitID, PatientID, VisitDate, Diagnosis)
# Run from the folder containing both CSV files
# =============================================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

# ── LOAD DATA ─────────────────────────────────────────────────────────────────
patients = pd.read_csv('patients.csv')
visits   = pd.read_csv('visits.csv')

print("patients.csv:")
print(patients)
print("\nvisits.csv:")
print(visits)


# =============================================================================
# PRACTICAL 8 – DATA CLEANING & MERGE
# =============================================================================
print("\n" + "="*60)
print("PRACTICAL 8 – CLEANING & MERGE (Patients & Visits)")
print("="*60)

# --- Clean patients ---
print("\n--- Clean patients ---")
print("Missing:\n", patients.isnull().sum())

# Age > 100 is invalid — replace with median
patients.loc[patients['Age'] > 100, 'Age'] = np.nan
patients['Age'] = patients['Age'].fillna(patients['Age'].median())
print("Age after fixing outlier:")
print(patients['Age'].values)

# Fill missing Age with median
patients['Age'] = patients['Age'].fillna(patients['Age'].median())

# Standardize Gender: M/Male -> Male, F/Female -> Female
gender_map = {'M': 'Male', 'F': 'Female', 'male': 'Male', 'female': 'Female'}
patients['Gender'] = patients['Gender'].replace(gender_map)
print("Patients after cleaning:")
print(patients)

# --- Clean visits ---
print("\n--- Clean visits ---")
print("Missing:\n", visits.isnull().sum())
visits['Diagnosis'] = visits['Diagnosis'].fillna('Unknown')
visits['VisitDate'] = pd.to_datetime(visits['VisitDate'], errors='coerce')
print("Visits after cleaning:")
print(visits)

# --- Merge ---
print("\n--- Merge ---")
df_inner = pd.merge(patients, visits, on='PatientID', how='inner')
print("Inner join (matched patients):")
print(df_inner)

df_left = pd.merge(patients, visits, on='PatientID', how='left')
print("\nLeft join (all patients):")
print(df_left)

df_outer = pd.merge(patients, visits, on='PatientID', how='outer')
print("\nOuter join (all records):")
print(df_outer)

# --- Analysis ---
print("\n--- Analysis ---")
print("Diagnoses:")
print(df_inner['Diagnosis'].value_counts())

print("\nAvg Age by Diagnosis:")
print(df_inner.groupby('Diagnosis')['Age'].mean().round(1))

# --- Visualization ---
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
gender_counts = patients['Gender'].value_counts()
plt.bar(gender_counts.index, gender_counts.values, color=['steelblue', 'coral'])
plt.ylabel('Count')
plt.title('Patient Count by Gender')

plt.subplot(1, 2, 2)
diag_counts = df_inner['Diagnosis'].value_counts()
plt.bar(diag_counts.index, diag_counts.values, color='seagreen')
plt.xticks(rotation=15)
plt.ylabel('Count')
plt.title('Diagnosis Frequency')

plt.tight_layout()
plt.show()

print("\n" + "="*60)
print("ALL PATIENTS PRACTICALS DONE")
print("="*60)
