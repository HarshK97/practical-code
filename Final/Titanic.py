# =============================================================================
# TITANIC DATASET - ALL PRACTICALS COMBINED
# Practical: 11
# Columns: PassengerId, Survived, Pclass, Name, Sex, Age, SibSp, Parch,
#          Ticket, Fare, Cabin, Embarked
# Run from the folder containing Titanic-Dataset.csv
# =============================================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
import warnings
warnings.filterwarnings('ignore')

# ── LOAD DATA ─────────────────────────────────────────────────────────────────
df = pd.read_csv('Titanic-Dataset.csv')

print("Dataset loaded. Shape:", df.shape)
print(df.head())
print("\nData Types:\n", df.dtypes)
print("\nMissing Values:\n", df.isnull().sum())
print("\nBasic Statistics:\n", df.describe())


# =============================================================================
# PRACTICAL 11 – DATA CLEANING & FEATURE ENGINEERING
# =============================================================================
print("\n" + "="*60)
print("PRACTICAL 11 – DATA CLEANING & FEATURE ENGINEERING")
print("="*60)

df11 = df.copy()

# --- Missing values ---
print("\nMissing before:")
print(df11.isnull().sum())

# Fill Age with median
df11['Age'] = df11['Age'].fillna(df11['Age'].median())

# Fill Embarked with mode
df11['Embarked'] = df11['Embarked'].fillna(df11['Embarked'].mode()[0])

# Drop Cabin (too many missing)
df11 = df11.drop(columns=['Cabin'])

print("\nMissing after:")
print(df11.isnull().sum())

# --- Remove unnecessary columns ---
df11 = df11.drop(columns=['PassengerId', 'Name', 'Ticket'])
print("\nColumns after drop:", df11.columns.tolist())

# --- Duplicates ---
print("Duplicates:", df11.duplicated().sum())

# --- Encoding ---
le = LabelEncoder()
df11['Sex_encoded']      = le.fit_transform(df11['Sex'])
df11['Embarked_encoded'] = LabelEncoder().fit_transform(df11['Embarked'])
print("\nSex encoding: male=", df11.loc[df11['Sex']=='male','Sex_encoded'].iloc[0],
      "female=", df11.loc[df11['Sex']=='female','Sex_encoded'].iloc[0])
print("Embarked unique:", df11[['Embarked','Embarked_encoded']].drop_duplicates().values)

# --- Feature Engineering ---
# Family size
df11['FamilySize'] = df11['SibSp'] + df11['Parch'] + 1
df11['IsAlone']    = (df11['FamilySize'] == 1).astype(int)

# Age category
df11['AgeGroup'] = pd.cut(df11['Age'], bins=[0,12,18,35,60,100],
                           labels=['Child','Teen','YoungAdult','Adult','Senior'])

# Fare category
df11['FareGroup'] = pd.cut(df11['Fare'], bins=[0,10,30,100,1000],
                            labels=['Low','Medium','High','VeryHigh'])

print("\nWith engineered features:")
print(df11[['Survived','Pclass','Sex','Age','AgeGroup','FamilySize','IsAlone','FareGroup']].head(10))

# --- Analysis ---
print("\n--- Analysis ---")
print("Survival rate overall:", df11['Survived'].mean().round(4))
print("\nSurvival by Sex:")
print(df11.groupby('Sex')['Survived'].mean().round(4))
print("\nSurvival by Pclass:")
print(df11.groupby('Pclass')['Survived'].mean().round(4))
print("\nSurvival by AgeGroup:")
print(df11.groupby('AgeGroup', observed=True)['Survived'].mean().round(4))

# --- Normalization ---
num_cols = ['Age', 'Fare', 'SibSp', 'Parch', 'FamilySize']
df11_mm = (df11[num_cols] - df11[num_cols].min()) / (df11[num_cols].max() - df11[num_cols].min())
print("\nMin-Max Normalized (Age, Fare):")
print(df11_mm[['Age','Fare']].describe().round(4))

# --- Outlier detection ---
print("\nOutlier Detection (IQR):")
for col in ['Age', 'Fare']:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    n = ((df[col] < Q1-1.5*IQR) | (df[col] > Q3+1.5*IQR)).sum()
    print(f"  {col}: {n} outliers")

# --- Visualization ---
plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
surv_counts = df11['Survived'].value_counts().sort_index()
plt.bar(['Not Survived', 'Survived'], surv_counts.values, color=['coral', 'steelblue'])
plt.ylabel('Count')
plt.title('Survival Count')

plt.subplot(1, 3, 2)
surv_by_class = df11.groupby('Pclass')['Survived'].mean()
plt.bar([f'Class {i}' for i in surv_by_class.index], surv_by_class.values, color='seagreen')
plt.ylabel('Survival Rate')
plt.title('Survival Rate by Class')

plt.subplot(1, 3, 3)
plt.hist(df11['Age'], bins=20, color='mediumpurple', edgecolor='white')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Age Distribution')

plt.tight_layout()
plt.show()

print("\n" + "="*60)
print("ALL TITANIC PRACTICALS DONE")
print("="*60)
