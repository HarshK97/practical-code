# =============================================================================
# EMPLOYEE INFO + PERFORMANCE - ALL PRACTICALS COMBINED
# Practical: 10
# Files: employee_info.csv (EmployeeID, Name, Department, Age, JoinDate)
#        performance.csv   (EmployeeID, ReviewScore1, ReviewScore2, EligiblePromotion)
# Run from the folder containing both CSV files
# =============================================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

# ── LOAD DATA ─────────────────────────────────────────────────────────────────
emp    = pd.read_csv('employee_info.csv')
perf   = pd.read_csv('performance.csv')

print("employee_info.csv:")
print(emp)
print("\nperformance.csv:")
print(perf)


# =============================================================================
# PRACTICAL 10 – CLEANING, MERGE & AGGREGATION
# =============================================================================
print("\n" + "="*60)
print("PRACTICAL 10 – CLEANING, MERGE & AGGREGATION")
print("="*60)

# --- Clean employee_info ---
print("\n--- Clean employee_info ---")
print("Missing:\n", emp.isnull().sum())

emp['Age'] = emp['Age'].fillna(emp['Age'].median())
emp['JoinDate'] = emp['JoinDate'].fillna('Unknown')

# Standardize Department (Sales vs sales)
emp['Department'] = emp['Department'].str.title().str.strip()
print("After cleaning:")
print(emp)

# --- Clean performance ---
print("\n--- Clean performance ---")
print("Missing:\n", perf.isnull().sum())
perf['AvgReview'] = (perf['ReviewScore1'] + perf['ReviewScore2']) / 2
print("After adding AvgReview:")
print(perf)

# --- Merge ---
print("\n--- Merge ---")
df_inner = pd.merge(emp, perf, on='EmployeeID', how='inner')
print("Inner join:")
print(df_inner)

df_outer = pd.merge(emp, perf, on='EmployeeID', how='outer')
print("\nOuter join (all employees):")
print(df_outer)

# --- Analysis ---
print("\n--- Analysis ---")
print("Sort by AvgReview (desc):")
print(df_inner.sort_values('AvgReview', ascending=False)[['Name','Department','AvgReview','EligiblePromotion']])

print("\nEligible for promotion:")
print(df_inner[df_inner['EligiblePromotion'] == 1][['Name','Department','AvgReview']])

print("\nAvg review by Department:")
print(df_inner.groupby('Department')['AvgReview'].mean().round(2))

# --- Feature engineering ---
df_inner['SeniorityFlag'] = df_inner['Age'].apply(lambda x: 'Senior' if x >= 35 else 'Junior')
print("\nWith Seniority Flag:")
print(df_inner[['Name','Age','SeniorityFlag','AvgReview']])

# --- Visualization ---
plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
dept_avg = df_inner.groupby('Department')['AvgReview'].mean()
plt.bar(dept_avg.index, dept_avg.values, color='steelblue')
plt.xticks(rotation=15)
plt.ylabel('Avg Review Score')
plt.title('Avg Review by Department')

plt.subplot(1, 2, 2)
promo = df_inner['EligiblePromotion'].value_counts()
plt.bar(['Not Eligible','Eligible'], promo.sort_index().values, color=['coral','seagreen'])
plt.ylabel('Count')
plt.title('Promotion Eligibility')

plt.tight_layout()
plt.show()

print("\n" + "="*60)
print("ALL EMPLOYEE PRACTICALS DONE")
print("="*60)
