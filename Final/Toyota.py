# =============================================================================
# TOYOTA DATASET - ALL PRACTICALS COMBINED
# Practicals: 5, 15, 18-27, 30-32
# Run from the folder containing Toyota.csv
# =============================================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, StandardScaler, LabelEncoder
import warnings
warnings.filterwarnings('ignore')

# ── LOAD DATA ─────────────────────────────────────────────────────────────────
df = pd.read_csv('Toyota.csv')

# Drop unnamed index column if present
if 'Unnamed: 0' in df.columns:
    df = df.drop(columns=['Unnamed: 0'])

# Fix mixed-type columns upfront so everything works cleanly
df['KM']  = pd.to_numeric(df['KM'],  errors='coerce')
df['HP']  = pd.to_numeric(df['HP'],  errors='coerce')
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')

print("Dataset loaded. Shape:", df.shape)
print(df.head())
print("\nData Types:\n", df.dtypes)
print("\nMissing Values:\n", df.isnull().sum())
print("\nBasic Statistics:\n", df.describe())


# =============================================================================
# PRACTICAL 5 – BASIC DATA OPERATIONS
# Subset | Merge | Sort | Transpose | Reshape
# =============================================================================
print("\n" + "="*60)
print("PRACTICAL 5 – BASIC DATA OPERATIONS")
print("="*60)

# a) Subset
subset1 = df.head(50)                              # first 50 rows
subset2 = df[['Price', 'Age', 'KM', 'FuelType']]  # select columns
subset3 = df[df['Price'] < 10000]                  # filter by condition
print("\na) Subsets:")
print("  First 50 rows:", subset1.shape)
print("  Selected columns:", subset2.shape)
print("  Price < 10000:", subset3.shape)

# b) Merge
df1 = df.iloc[:100].copy()
df2 = df.iloc[100:200].copy()
df_merged = pd.concat([df1, df2], ignore_index=True)
print("\nb) Merge:", df1.shape, "+", df2.shape, "=", df_merged.shape)

# c) Sort
df_sorted = df.sort_values('Price', ascending=False)
print("\nc) Sort by Price (top 5):")
print(df_sorted[['Price', 'Age', 'KM']].head())

# d) Transpose
sample = df.head(5)
print("\nd) Transpose:", sample.shape, "->", sample.T.shape)
print(sample.T)

# e) Shape / Reshape (melt)
print("\ne) Shape:", df.shape, "| Size:", df.size)
df_melt = pd.melt(df[['Price', 'Age', 'KM']].head(5).reset_index(),
                  id_vars='index', value_vars=['Price', 'Age', 'KM'])
print("Melt sample:\n", df_melt)


# =============================================================================
# PRACTICAL 15 – DATA CLEANING & INTEGRATION
# =============================================================================
print("\n" + "="*60)
print("PRACTICAL 15 – DATA CLEANING & INTEGRATION")
print("="*60)

df_clean = df.copy()

# Missing values
print("\nMissing before:\n", df_clean.isnull().sum())

for col in df_clean.select_dtypes(include=[np.number]).columns:
    df_clean[col] = df_clean[col].fillna(df_clean[col].median())

for col in df_clean.select_dtypes(include='object').columns:
    df_clean[col] = df_clean[col].fillna(df_clean[col].mode()[0])

print("Missing after:", df_clean.isnull().sum().sum())

# Duplicates
print("Duplicates:", df_clean.duplicated().sum())
df_clean = df_clean.drop_duplicates()

# Fix Doors column (has 'three', 'four', etc.)
door_map = {'two': 2, 'three': 3, 'four': 4, 'five': 5}
df_clean['Doors'] = df_clean['Doors'].replace(door_map)
df_clean['Doors'] = pd.to_numeric(df_clean['Doors'], errors='coerce').fillna(4)
print("Doors unique:", df_clean['Doors'].unique())

# Outlier detection – IQR
print("\nOutlier Detection (IQR):")
for col in ['Price', 'KM', 'Age']:
    Q1 = df_clean[col].quantile(0.25)
    Q3 = df_clean[col].quantile(0.75)
    IQR = Q3 - Q1
    n = ((df_clean[col] < Q1 - 1.5*IQR) | (df_clean[col] > Q3 + 1.5*IQR)).sum()
    print(f"  {col}: {n} outliers  (Q1={Q1:.1f}, Q3={Q3:.1f}, IQR={IQR:.1f})")

print("\nCleaned shape:", df_clean.shape)


# =============================================================================
# PRACTICAL 18 – MISSING VALUE HANDLING
# =============================================================================
print("\n" + "="*60)
print("PRACTICAL 18 – MISSING VALUE HANDLING")
print("="*60)

df18 = df.copy()

# Introduce some missing values to demonstrate
np.random.seed(0)
idx = np.random.choice(df18.index, 20, replace=False)
df18.loc[idx[:10], 'Price']    = np.nan
df18.loc[idx[10:], 'FuelType'] = np.nan

print("Missing introduced:\n", df18.isnull().sum())

# 1. Drop rows with any missing
print("After dropna:", df18.dropna().shape)

# 2. Fill with mean / median / mode
df18['Price']    = df18['Price'].fillna(df18['Price'].mean())
df18['FuelType'] = df18['FuelType'].fillna(df18['FuelType'].mode()[0])
print("Missing after fill:", df18.isnull().sum().sum())

# 3. Forward fill
df18 = df18.ffill()
print("Missing after ffill:", df18.isnull().sum().sum())


# =============================================================================
# PRACTICAL 19 – DATA TYPE CONVERSION
# =============================================================================
print("\n" + "="*60)
print("PRACTICAL 19 – DATA TYPE CONVERSION")
print("="*60)

df19 = df.copy()
print("Before:\n", df19.dtypes)

df19['MetColor']  = df19['MetColor'].fillna(0).astype(int)
df19['Automatic'] = df19['Automatic'].astype(bool)

le = LabelEncoder()
df19['FuelType_encoded'] = le.fit_transform(df19['FuelType'].astype(str))
print("\nFuelType encoding:", dict(zip(le.classes_, le.transform(le.classes_))))

door_map2 = {'two': 2, 'three': 3, 'four': 4, 'five': 5}
df19['Doors'] = df19['Doors'].replace(door_map2)
df19['Doors'] = pd.to_numeric(df19['Doors'], errors='coerce').fillna(4).astype(int)

print("\nAfter:\n", df19[['MetColor','Automatic','FuelType_encoded','Doors']].dtypes)
print(df19[['FuelType','FuelType_encoded','Doors','MetColor','Automatic']].head())


# =============================================================================
# PRACTICAL 20 – SUBSETTING & FILTERING
# =============================================================================
print("\n" + "="*60)
print("PRACTICAL 20 – SUBSETTING & FILTERING")
print("="*60)

petrol  = df[df['FuelType'] == 'Petrol']
diesel  = df[df['FuelType'] == 'Diesel']
print("Petrol cars:", len(petrol), "| Diesel cars:", len(diesel))

young_cheap = df[(df['Age'] < 30) & (df['Price'] < 12000)]
print("Age<30 & Price<12000:", len(young_cheap))

low_km  = df[df['KM'] < 50000]
high_km = df[df['KM'] > 150000]
print("Low KM (<50k):", len(low_km), "| High KM (>150k):", len(high_km))

print("\nisin filter (Petrol or Diesel):", len(df[df['FuelType'].isin(['Petrol','Diesel'])]))

print("\niloc (rows 0-2, cols 0-3):\n", df.iloc[0:3, 0:4])
print("\nloc (Price > 20000):\n", df.loc[df['Price'] > 20000, ['Price','Age','KM']].head())


# =============================================================================
# PRACTICAL 21 – SORTING & RANKING
# =============================================================================
print("\n" + "="*60)
print("PRACTICAL 21 – SORTING & RANKING")
print("="*60)

print("Cheapest 5:\n", df.sort_values('Price')[['Price','Age','KM']].head())
print("\nMost expensive 5:\n", df.sort_values('Price', ascending=False)[['Price','Age','KM']].head())
print("\nSorted by FuelType ASC, Price DESC:\n",
      df.sort_values(['FuelType','Price'], ascending=[True,False])[['FuelType','Price','Age']].head(6))

df_r = df.copy()
df_r['Rank'] = df_r['Price'].rank(ascending=False).astype(int)
print("\nTop 5 by rank:\n", df_r.sort_values('Rank')[['Price','Rank','Age']].head())


# =============================================================================
# PRACTICAL 22 – GROUPING & AGGREGATION
# =============================================================================
print("\n" + "="*60)
print("PRACTICAL 22 – GROUPING & AGGREGATION")
print("="*60)

fuel_grp = df.groupby('FuelType').agg(
    Count    = ('Price', 'count'),
    Avg_Price= ('Price', 'mean'),
    Max_Price= ('Price', 'max'),
    Avg_KM   = ('KM',    'mean'),
    Avg_Age  = ('Age',   'mean')
).round(2)
print("By FuelType:\n", fuel_grp)

auto_grp = df.groupby('Automatic')[['Price','KM','HP']].mean().round(2)
print("\nBy Automatic:\n", auto_grp)


# =============================================================================
# PRACTICAL 23 – MIN-MAX NORMALIZATION
# =============================================================================
print("\n" + "="*60)
print("PRACTICAL 23 – MIN-MAX NORMALIZATION")
print("="*60)

num_cols = ['Price', 'Age', 'KM', 'HP', 'CC', 'Weight']
df23 = df[num_cols].dropna()

# Manual formula
df_mm = (df23 - df23.min()) / (df23.max() - df23.min())
print("Manual Min-Max (Price):")
print(f"  min={df_mm['Price'].min():.4f}, max={df_mm['Price'].max():.4f}, mean={df_mm['Price'].mean():.4f}")
print(df_mm.head())

# sklearn
scaler = MinMaxScaler()
df_mm_sk = pd.DataFrame(scaler.fit_transform(df23), columns=num_cols)
print("\nsklearn MinMaxScaler:\n", df_mm_sk.describe().round(4))


# =============================================================================
# PRACTICAL 24 – Z-SCORE STANDARDIZATION
# =============================================================================
print("\n" + "="*60)
print("PRACTICAL 24 – Z-SCORE STANDARDIZATION")
print("="*60)

df24 = df[num_cols].dropna()

# Manual formula
df_zs = (df24 - df24.mean()) / df24.std()
print("Manual Z-Score (Price):")
print(f"  mean={df_zs['Price'].mean():.4f}, std={df_zs['Price'].std():.4f}")
print(df_zs.head())

# sklearn
std_scaler = StandardScaler()
df_zs_sk = pd.DataFrame(std_scaler.fit_transform(df24), columns=num_cols)
print("\nsklearn StandardScaler:\n", df_zs_sk.describe().round(4))


# =============================================================================
# PRACTICAL 25 – DECIMAL SCALING NORMALIZATION
# =============================================================================
print("\n" + "="*60)
print("PRACTICAL 25 – DECIMAL SCALING NORMALIZATION")
print("="*60)

df25 = df[num_cols].dropna().copy()
df_dec = df25.copy()

print("Decimal scaling divisors:")
for col in num_cols:
    j = int(np.ceil(np.log10(df25[col].abs().max() + 1)))
    df_dec[col] = df25[col] / (10 ** j)
    print(f"  {col}: divide by 10^{j} = {10**j}")

print("\nAfter Decimal Scaling:\n", df_dec.head())


# =============================================================================
# PRACTICAL 26 – ENCODING CATEGORICAL VARIABLES
# =============================================================================
print("\n" + "="*60)
print("PRACTICAL 26 – ENCODING CATEGORICAL VARIABLES")
print("="*60)

df26 = df.copy()

# Label Encoding
le26 = LabelEncoder()
df26['FuelType_Label'] = le26.fit_transform(df26['FuelType'].astype(str))
print("Label Encoding:", dict(zip(le26.classes_, le26.transform(le26.classes_))))

# One-Hot Encoding
df_ohe = pd.get_dummies(df26['FuelType'], prefix='Fuel')
df26 = pd.concat([df26, df_ohe], axis=1)
print("\nOne-Hot Encoding sample:")
print(df26[['FuelType','FuelType_Label','Fuel_CNG','Fuel_Diesel','Fuel_Petrol']].head())


# =============================================================================
# PRACTICAL 27 – FEATURE ENGINEERING
# =============================================================================
print("\n" + "="*60)
print("PRACTICAL 27 – FEATURE ENGINEERING")
print("="*60)

df27 = df.copy()

df27['Price_per_KM'] = (df27['Price'] / (df27['KM'] + 1)).round(4)
print("Price per KM:\n", df27[['Price','KM','Price_per_KM']].head())

df27['Age_Category'] = pd.cut(df27['Age'], bins=[0,24,60,300],
                               labels=['New','Mid','Old'])
print("\nAge Category:\n", df27['Age_Category'].value_counts())

df27['KM_Category'] = pd.cut(df27['KM'], bins=[0,50000,150000,1e9],
                              labels=['Low','Medium','High'])
print("\nKM Category:\n", df27['KM_Category'].value_counts())

df27['KM_log'] = np.log1p(df27['KM'])
print(f"\nKM skew  original: {df27['KM'].skew():.4f}")
print(f"KM skew log-transform: {df27['KM_log'].skew():.4f}")


# =============================================================================
# PRACTICAL 30 – SCATTER PLOTS
# =============================================================================
print("\n" + "="*60)
print("PRACTICAL 30 – SCATTER PLOTS")
print("="*60)

plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.scatter(df['Age'], df['Price'], alpha=0.4, color='steelblue', s=10)
plt.xlabel('Age (months)')
plt.ylabel('Price')
plt.title('Price vs Age')

plt.subplot(1, 3, 2)
plt.scatter(df['KM'], df['Price'], alpha=0.4, color='coral', s=10)
plt.xlabel('KM')
plt.ylabel('Price')
plt.title('Price vs KM')

plt.subplot(1, 3, 3)
plt.scatter(df['HP'], df['Price'], alpha=0.4, color='seagreen', s=10)
plt.xlabel('HP')
plt.ylabel('Price')
plt.title('Price vs HP')

plt.tight_layout()
plt.show()


# =============================================================================
# PRACTICAL 31 – HISTOGRAMS
# =============================================================================
print("\n" + "="*60)
print("PRACTICAL 31 – HISTOGRAMS")
print("="*60)

plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.hist(df['Price'].dropna(), bins=30, color='steelblue', edgecolor='white')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.title('Price Distribution')

plt.subplot(1, 3, 2)
plt.hist(df['Age'].dropna(), bins=30, color='coral', edgecolor='white')
plt.xlabel('Age (months)')
plt.ylabel('Frequency')
plt.title('Age Distribution')

plt.subplot(1, 3, 3)
plt.hist(df['KM'].dropna(), bins=30, color='seagreen', edgecolor='white')
plt.xlabel('KM')
plt.ylabel('Frequency')
plt.title('KM Distribution')

plt.tight_layout()
plt.show()


# =============================================================================
# PRACTICAL 32 – BAR PLOTS
# =============================================================================
print("\n" + "="*60)
print("PRACTICAL 32 – BAR PLOTS")
print("="*60)

plt.figure(figsize=(12, 4))

# Count by FuelType
plt.subplot(1, 3, 1)
counts = df['FuelType'].value_counts()
plt.bar(counts.index, counts.values, color=['steelblue','coral','seagreen'])
plt.xlabel('FuelType')
plt.ylabel('Count')
plt.title('Count by FuelType')

# Avg Price by FuelType
plt.subplot(1, 3, 2)
avg_price = df.groupby('FuelType')['Price'].mean()
plt.bar(avg_price.index, avg_price.values, color='mediumpurple')
plt.xlabel('FuelType')
plt.ylabel('Avg Price')
plt.title('Avg Price by FuelType')

# Avg KM by FuelType
plt.subplot(1, 3, 3)
avg_km = df.groupby('FuelType')['KM'].mean()
plt.bar(avg_km.index, avg_km.values, color='goldenrod')
plt.xlabel('FuelType')
plt.ylabel('Avg KM')
plt.title('Avg KM by FuelType')

plt.tight_layout()
plt.show()

print("\n" + "="*60)
print("ALL PRACTICALS DONE")
print("="*60)
