\* { box-sizing: border-box; margin: 0; padding: 0 } .wrap { padding: 1rem 0; font-family: var(--font-sans) } .tabs { display: flex; gap: 6px; flex-wrap: wrap; margin-bottom: 1.25rem } .tab { padding: 6px 13px; border-radius: var(--border-radius-md); border: 0.5px solid var(--color-border-secondary); background: transparent; font-size: 12px; cursor: pointer; color: var(--color-text-secondary); transition: all .15s } .tab.active { background: var(--color-background-secondary); color: var(--color-text-primary); border-color: var(--color-border-primary); font-weight: 500 } .section { display: none } .section.active { display: block } .card { background: var(--color-background-primary); border: 0.5px solid var(--color-border-tertiary); border-radius: var(--border-radius-lg); padding: .9rem 1.1rem; margin-bottom: .65rem; cursor: pointer } .card-hdr { display: flex; justify-content: space-between; align-items: center; gap: 8px } .card-title { font-size: 14px; font-weight: 500; color: var(--color-text-primary) } .card-meta { display: flex; gap: 6px; align-items: center; flex-shrink: 0 } .badge { font-size: 11px; padding: 2px 7px; border-radius: var(--border-radius-md) } .b-blue { background: #E6F1FB; color: #0C447C } .b-green { background: #E1F5EE; color: #085041 } .b-coral { background: #FAECE7; color: #712B13 } .b-gray { background: #F1EFE8; color: #444441 } .b-purple { background: #EEEDFE; color: #3C3489 } .chevron { font-size: 17px; color: var(--color-text-tertiary); transition: transform .2s; flex-shrink: 0 } .chevron.open { transform: rotate(180deg) } .card-body { display: none; margin-top: .75rem; border-top: 0.5px solid var(--color-border-tertiary); padding-top: .75rem } .card-body.open { display: block } .qa { margin-bottom: .7rem } .q { font-size: 13px; font-weight: 500; color: var(--color-text-primary); margin-bottom: .3rem } .a { font-size: 13px; color: var(--color-text-secondary); line-height: 1.65 } pre { background: var(--color-background-secondary); border: 0.5px solid var(--color-border-tertiary); border-radius: var(--border-radius-md); padding: .7rem .9rem; font-size: 12px; font-family: var(--font-mono); overflow-x: auto; white-space: pre; margin: .5rem 0; color: var(--color-text-primary) } .prog-label { font-size: 12px; color: var(--color-text-secondary); margin-bottom: 5px } .prog-bar { background: var(--color-background-secondary); border-radius: 99px; height: 5px; margin-bottom: 1rem } .prog-fill { height: 5px; border-radius: 99px; background: #1D9E75; transition: width .3s } .search-wrap { margin-bottom: 1rem } .search-wrap input { width: 100%; padding: 8px 12px; border-radius: var(--border-radius-md); border: 0.5px solid var(--color-border-secondary); background: var(--color-background-primary); color: var(--color-text-primary); font-size: 13px } .no-results { font-size: 13px; color: var(--color-text-tertiary); padding: .5rem 0 } .qf-card { background: var(--color-background-primary); border: 0.5px solid var(--color-border-tertiary); border-radius: var(--border-radius-lg); padding: 1.2rem; min-height: 110px; cursor: pointer; margin-bottom: .75rem } .qf-q { font-size: 14px; font-weight: 500; color: var(--color-text-primary); margin-bottom: .5rem } .qf-a { font-size: 13px; color: var(--color-text-secondary); line-height: 1.6; display: none } .qf-hint { font-size: 11px; color: var(--color-text-tertiary); margin-top: .5rem }

## DSBDA complete oral and practical exam prep — theory, code, and official FAQ answers

Official FAQs Hadoop Pandas ops Data cleaning Visualization Normalization Quick fire

1\. Big Data and its characteristicscore

What is Big Data?

Data that is too large, fast, or complex for traditional systems to process. Comes from social media, IoT sensors, transactions, logs etc.

5 Vs (characteristics):

**Volume** — massive scale (TBs/PBs). **Velocity** — speed of generation and processing. **Variety** — structured, semi-structured, unstructured. **Veracity** — trustworthiness/quality. **Value** — business value extracted. The 4Vs as challenges: high volume overwhelms storage, high velocity needs real-time processing, variety makes integration hard, veracity causes garbage-in-garbage-out.

2\. GFS componentshadoop

What is GFS and how does it relate to HDFS?

Google File System (GFS) is Google's proprietary distributed file system — the inspiration for HDFS. Components: **Master** (like NameNode) — stores metadata, manages namespace. **ChunkServers** (like DataNodes) — store data in 64MB chunks. **Clients** — access data by querying master for chunk locations then reading directly from chunkservers. Key design: large chunk size, single master, replication for fault tolerance.

3\. Hadoop frameworkhadoop

Explain the Hadoop framework.

Hadoop is an open-source framework for distributed storage and processing of large datasets. Three core layers: **HDFS** — storage layer, distributes data across nodes. **MapReduce** — processing layer, runs parallel computations. **YARN** — resource management layer, allocates CPU/memory to jobs. Philosophy: move computation to data (not data to computation) to minimize network traffic.

4\. Cluster of commodity hardwarehadoop

What is a commodity hardware cluster?

A cluster of many low-cost, standard (off-the-shelf) machines networked together — as opposed to expensive specialized servers. Hadoop is designed to run on commodity hardware and handle node failures gracefully through replication, making it cost-effective for big data storage and processing.

5\. HDFS components — NameNode, SNN, DataNodehadoop

Explain each HDFS component.

**NameNode (Master):** Stores file system metadata — directory tree, file-to-block mappings, block locations. Does NOT store actual data. Single point of failure (hence SNN). **Secondary NameNode (SNN):** Periodically merges the FSImage and EditLog to create a new FSImage. NOT a backup NameNode — just helps reduce NameNode restart time. **DataNode (Worker):** Stores actual data blocks (128MB default), sends heartbeats to NameNode every 3 seconds, replicates blocks to other DataNodes. Default replication = 3.

6\. YARN — ResourceManager and NodeManagerhadoop

Explain YARN's components.

**ResourceManager (Master):** Global resource arbiter — accepts job submissions, allocates resources (CPU, memory containers) across the cluster. Has a Scheduler and ApplicationManager. **NodeManager (Worker):** Per-node agent — monitors container resource usage, reports to ResourceManager, kills containers that exceed limits. **ApplicationMaster:** Per-application process — negotiates resources from RM, works with NMs to execute and monitor tasks.

7\. Fault tolerance, durability, parallel processinghadoop

How does Hadoop achieve these three?

**Fault tolerance:** Each block replicated 3x across different nodes/racks. If a DataNode fails, NameNode detects missing heartbeat and instructs re-replication from surviving copies. **Data durability:** Data persists even after node failures due to replication. HDFS write-once model prevents corruption. **Parallel processing:** MapReduce splits input into chunks processed simultaneously by multiple mappers across the cluster. Data locality — mapper runs on same node as its data block, minimizing network I/O.

8\. MapReducehadoop

Explain MapReduce with an example.

**Map phase:** Input split into chunks → Mapper reads records, emits (key, value) pairs. **Shuffle & Sort:** Framework groups all values with same key, sorts keys. **Reduce phase:** Reducer receives (key, \[list of values\]), aggregates and emits final output.

Word count example: Input "hello world hello" → Mapper emits ("hello",1),("world",1),("hello",1) → Shuffle groups: ("hello",\[1,1\]),("world",\[1\]) → Reducer: ("hello",2),("world",1)

9\. How data files are stored on HDFShadoop

Walk through how a file gets stored in HDFS.

1\. Client contacts NameNode to create file. 2. NameNode checks permissions, returns block IDs + DataNode locations. 3. Client writes block 1 to DataNode-1 which pipelines it to DataNode-2 → DataNode-3 (replication pipeline). 4. After each block is written, client gets acknowledgment. 5. NameNode updates metadata with block→DataNode mapping. Default block size: 128MB. A 300MB file = 3 blocks spread across nodes.

10\. Hadoop ecosystem toolshadoop

Name and explain key Hadoop ecosystem tools.

**Hive:** SQL-like querying on HDFS data using HiveQL. Good for batch analytics. **HBase:** NoSQL, column-family database on HDFS. Real-time random read/write access. **Pig:** High-level data flow scripting language (Pig Latin) that compiles to MapReduce. **Sqoop:** Import/export data between RDBMS and HDFS. **Flume:** Real-time log/event data ingestion into HDFS. **Spark:** In-memory processing engine, 100x faster than MapReduce for iterative jobs.

11\. Pandas DataFrame — datatypes, attributes, methodspython

Key Pandas DataFrame attributes and methods?

**Attributes:** df.shape (rows,cols), df.dtypes, df.columns, df.index, df.size, df.ndim  
**Info methods:** df.info(), df.describe(), df.head(n), df.tail(n)  
**Cleaning:** df.isnull(), df.dropna(), df.fillna(), df.duplicated(), df.drop_duplicates()  
**Selection:** df\['col'\], df\[\['c1','c2'\]\], df.loc\[\], df.iloc\[\]  
**Reshape:** df.melt(), df.pivot(), df.pivot_table(), df.T (transpose)  
**Aggregation:** df.groupby(), df.agg(), df.apply()

12 & 13. Tableau features and panestableau

Tableau panes and key features?

**Panes:** Data pane (left — lists dimensions & measures), Shelves (Columns, Rows, Pages, Filters, Marks), Canvas/View (center — the viz), Show Me panel (right — chart type suggestions).  
**Features:** Drag-and-drop viz, live/extract connections, calculated fields, parameters, sets, groups, dual-axis charts, reference lines, forecasting, story points.  
**Project stages in DV:** 1. Connect to data, 2. Prepare/clean, 3. Explore (EDA), 4. Build visualizations, 5. Create dashboard, 6. Publish/share.

14\. Measures and dimensionstableau

What are measures and dimensions in Tableau?

**Dimensions:** Categorical/qualitative fields used to slice and group data — e.g. Region, Category, Gender, Date. Blue pills in Tableau. **Measures:** Numeric/quantitative fields that can be aggregated — e.g. Sales, Profit, Age, Score. Green pills. Tableau auto-classifies: text/date → dimension, number → measure. You can manually convert. Dimensions go on Rows/Columns shelves to create headers; Measures go to view to create axes.

15\. Measures of central tendencystats

Define mean, median, and mode with when to use each.

**Mean:** Sum of values / count. Sensitive to outliers. Use when data is normally distributed with no outliers. **Median:** Middle value when sorted. Robust to outliers. Use for skewed data (e.g. house prices, income). **Mode:** Most frequent value. Use for categorical data (e.g. most common fuel type). Example: \[1,2,3,100\] — Mean=26.5 (misleading), Median=2.5 (better), Mode=none.

16\. Why normalize? 3 ways of normalizationstats

Why is normalization required and what are the 3 methods?

**Why:** Features with large ranges dominate distance-based algorithms (KNN, SVM). Normalization puts all features on same scale for fair comparison and faster convergence in ML.  
**1\. Min-Max (0 to 1):** x' = (x - min) / (max - min). Use when you know bounds and want exact range.  
**2\. Z-score (Standardization):** x' = (x - mean) / std. Use when data is normally distributed; output has mean=0, std=1.  
**3\. Decimal Scaling:** x' = x / 10^j where j is smallest integer making max(|x'|) < 1. Simple, works on any scale.

17\. CAP theoremtheory

Explain CAP theorem.

Brewer's theorem: A distributed system can only guarantee 2 of these 3 properties simultaneously. **Consistency (C):** Every read gets the most recent write. **Availability (A):** Every request gets a response (may not be latest). **Partition tolerance (P):** System works despite network partitions. Since network partitions always happen in real distributed systems, you choose CA or CP or AP. HDFS = CP (consistent + partition tolerant, can be unavailable if NameNode down). Cassandra = AP. RDBMS (single node) = CA.

18\. NoSQL databasestheory

What are NoSQL databases? Types with examples.

Databases designed for unstructured/semi-structured data, horizontal scaling, and flexible schemas — unlike RDBMS. 4 types: **Key-Value:** Redis, DynamoDB — fast lookups by key. **Document:** MongoDB, CouchDB — stores JSON-like documents. **Column-family:** HBase, Cassandra — optimized for column-oriented queries on wide tables. **Graph:** Neo4j — stores nodes and edges, great for social networks. NoSQL = "Not Only SQL" — can have some SQL-like querying.

19 & 20. Data visualization — objectives, tools, chart typestableau

What is data visualization? Objectives and tools?

**Definition:** Visual representation of data to communicate insights clearly using charts, graphs, maps, dashboards.  
**Objectives:** Identify patterns/trends, spot outliers, communicate complex data simply, support decision-making, explore relationships.  
**Tools:** Tableau, MS Power BI, Helical Insight, Google Data Studio, matplotlib, seaborn, D3.js.  
**Chart types & purpose:** Bar — comparison. Line — trends over time. Scatter — correlation. Pie — proportions. Heatmap — correlations between many variables. Box plot — distribution and outliers. Histogram — frequency distribution. Treemap — hierarchical proportions.

21\. Dashboard — insights and decision makingtableau

What is a dashboard and why is it useful?

A dashboard is a single visual display that consolidates multiple charts/KPIs from related data sources for at-a-glance monitoring. Useful because: shows multiple metrics simultaneously, allows interactive filtering/drill-down, highlights trends and anomalies, enables faster decisions without reading raw data. Example: Tableau Superstore dashboard showing Sales + Profit + Quantity by Region with state-level map — a manager can instantly see underperforming regions and drill into specific product categories.

22\. Phases of a data science projecttheory

What are the phases of a data science project?

1\. **Problem definition** — understand business objective. 2. **Data collection** — gather from databases, APIs, scraping. 3. **Data preprocessing** — clean, integrate, transform. 4. **EDA (Exploratory Data Analysis)** — stats, visualization to understand patterns. 5. **Model building** — select algorithm, train model. 6. **Model evaluation** — accuracy, precision, recall, etc. 7. **Deployment** — integrate into production. 8. **Monitoring** — track performance over time.

0 of 3 reviewed

A1 — Hadoop installation & HDFS commandsbash

3 modes of Hadoop?

Standalone (no HDFS, single JVM), Pseudo-distributed (all daemons on one machine, simulates cluster), Fully distributed (multiple physical machines, production).

Setup & verification commands:

hdfs namenode -format # format once only
start-dfs.sh # start NameNode + DataNode
start-yarn.sh # start ResourceManager + NodeManager
jps # verify daemons running

hdfs dfs -mkdir /user/input
hdfs dfs -put logfile.txt /user/input/
hdfs dfs -ls /user/input
hdfs dfs -cat /output/part-r-00000
hdfs dfs -get /output/part-r-00000 ./result.txt

A2 — MapReduce log file (Java)java

Find users with maximum login time from log file:

// Mapper.java
public void map(LongWritable key, Text value, Context ctx) {
String\[\] parts = value.toString().split(",");
// parts\[0\]=username, parts\[1\]=duration
ctx.write(new Text(parts\[0\]),
new LongWritable(Long.parseLong(parts\[1\])));
}

// Reducer.java
public void reduce(Text key, Iterable<LongWritable> vals, Context ctx){
long total = 0;
for(LongWritable v : vals) total += v.get();
ctx.write(key, new LongWritable(total));
}

// Run:
// hadoop jar LoginCount.jar LogDriver /user/input /user/output

Oral: what does the reducer receive?

After shuffle-sort, reducer gets each unique key paired with an iterable list of all values emitted for that key by all mappers. E.g. ("alice", \[120, 45, 60\]).

A3 — HiveQL flight information systemhiveql

\-- Create database and table
CREATE DATABASE flights_db;
USE flights_db;

CREATE EXTERNAL TABLE flights (
Year INT, Month INT, DayOfMonth INT,
DepDelay INT, ArrDelay INT, Origin STRING, Dest STRING
)
ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
STORED AS TEXTFILE
LOCATION '/user/hive/flights/';

-- Load data
LOAD DATA INPATH '/user/input/flights.csv' INTO TABLE flights;

-- Create index
CREATE INDEX idx_origin ON TABLE flights(Origin)
AS 'COMPACT' WITH DEFERRED REBUILD;

-- Average departure delay per day in 2008
SELECT DayOfMonth, AVG(DepDelay) AS avg_delay
FROM flights
WHERE Year = 2008
GROUP BY DayOfMonth
ORDER BY DayOfMonth;

-- Drop and alter
ALTER TABLE flights ADD COLUMNS (FlightNum INT);
DROP TABLE IF EXISTS flights;

Managed vs External table?

Managed: drop table deletes data from HDFS. External: drop table only removes metadata, HDFS data safe. Use external when data is shared with other tools.

0 of 4 reviewed

B1 — Iris / Toyota / Facebook: subset, merge, sort, transpose, reshapepython

import pandas as pd

df = pd.read_csv('Iris.csv')

# Always start — understand the dataset

print(df.shape, df.dtypes, df.describe())
print(df.isnull().sum(), df.duplicated().sum())

# a. Subset

subset = df\[(df\['petal_length'\] > 1.5) & (df\['species'\] == 'setosa')\]

# b. Merge with custom table

species_info = pd.DataFrame({
'species': \['setosa','versicolor','virginica'\],
'color': \['blue','green','red'\]
})
merged = pd.merge(df, species_info, on='species', how='left')

# c. Sort (multi-column)

sorted_df = df.sort_values(\['sepal_width','sepal_length'\],
ascending=\[True, True\])

# d. Transpose first 5 rows

transposed = df.head(5).T
print(transposed)

# e. Reshape — melt (wide → long)

melted = df.melt(id_vars=\['species'\],
var_name='feature', value_name='value')

# pivot (long → wide)

pivoted = melted.pivot_table(index='species',
columns='feature',
values='value', aggfunc='mean')

Toyota.csv — all common operationspython

import pandas as pd
import numpy as np

df = pd.read_csv('Toyota.csv')

# Remove missing values

df_clean = df.dropna()

# OR fill with appropriate value

df\['Age'\].fillna(df\['Age'\].median(), inplace=True)
df\['FuelType'\].fillna('Petrol', inplace=True)

# Standardize Doors column

print(df\['Doors'\].unique()) # check values like '3','four',4
df\['Doors'\] = df\['Doors'\].replace({'three':3,'four':4,'five':5})
df\['Doors'\] = pd.to_numeric(df\['Doors'\], errors='coerce')

# Remove duplicates

df.drop_duplicates(inplace=True)

# Summary of numeric variables

print(df.describe())
print(df.dtypes)

# One-hot encoding for FuelType

df = pd.get_dummies(df, columns=\['FuelType'\])

# Add revised price column (5% increase)

df\['Revised'\] = df\['Price'\] \* 1.05

# Subset: Price > 15000 and Age < 8

expensive_new = df\[(df\['Price'\] > 15000) & (df\['Age'\] < 8)\]

# Subset petrol cars

petrol = df\[df\['FuelType_Petrol'\] == 1\]

# Sort by Price descending

df_sorted = df.sort_values('Price', ascending=False)

# Pivot table

pt = df.pivot_table(values='Price', index='FuelType',
aggfunc=\['mean','count'\])

Salaries.csv — filtering with conditionspython

import pandas as pd
df = pd.read_csv('Salaries.csv')

# Columns: rank, discipline, yrs.service, yrs.since.phd, sex, salary

# a. Staff NOT in discipline A

not_A = df\[df\['discipline'\] != 'A'\]\[\['rank','salary'\]\]

# b. All male staff + only female professors

male = df\[df\['sex'\] == 'Male'\]\[\['rank','salary','yrs.service'\]\]
female_prof = df\[(df\['sex'\]=='Female') & (df\['rank'\]=='Prof')\]
result_b = pd.concat(\[male, female_prof\[\['rank','salary','yrs.service'\]\]\])

# c. Female staff: professor OR salary > 75000

female_special = df\[
(df\['sex'\] == 'Female') &
((df\['rank'\] == 'Prof') | (df\['salary'\] > 75000))
\]

# d. Non-professors serving >= 10 years

result_d = df\[
(df\['rank'\] != 'Prof') & (df\['yrs.service'\] >= 10)
\]\[\['rank','salary'\]\]

Airquality dataset operationspython

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('airquality.csv')
print(df.head(), df.describe(), df.isnull().sum())

# b. Subset rows 11-49 and Temp < 60

subset1 = df.iloc\[10:49\] # rows 11 to 49 (0-indexed)
subset2 = df\[df\['Temp'\] < 60\]

# c. Merge two subsets

merged = pd.concat(\[subset1, subset2\]).drop_duplicates()

# d. Sort by Temp

sorted_df = df.sort_values('Temp')

# Select specific columns

cols_df = df\[\['Ozone','Solar.R','Wind','Temp'\]\]

# Replace NaN rationally (median for numeric)

df\['Ozone'\].fillna(df\['Ozone'\].median(), inplace=True)
df\['Solar.R'\].fillna(df\['Solar.R'\].mean(), inplace=True)

# Min-max normalization on Solar.R

df\['Solar_norm'\] = (df\['Solar.R'\] - df\['Solar.R'\].min()) / \\
(df\['Solar.R'\].max() - df\['Solar.R'\].min())

# Month-wise temperature plot

plt.figure(figsize=(8,4))
sns.lineplot(data=df, x='Month', y='Temp', estimator='mean')
plt.title('Month-wise Average Temperature')
plt.show()

0 of 4 reviewed

Titanic — imputation, encoding, feature engineeringcleaning

import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('Titanic-Dataset.csv')

# a. Handle missing Age and Cabin

df\['Age'\].fillna(df\['Age'\].median(), inplace=True)
df\['Cabin'\].fillna('Unknown', inplace=True)

# OR drop Cabin (too many missing)

df.drop(columns=\['Cabin'\], inplace=True)

# b. Encode Sex and Embarked

le = LabelEncoder()
df\['Sex_enc'\] = le.fit_transform(df\['Sex'\]) # male=1, female=0
df\['Embarked'\].fillna(df\['Embarked'\].mode()\[0\], inplace=True)
df\['Embarked_enc'\] = le.fit_transform(df\['Embarked'\])

# c. New feature: FamilySize

df\['FamilySize'\] = df\['SibSp'\] + df\['Parch'\]

# d. Bin Fare into categories

df\['FareCategory'\] = pd.cut(df\['Fare'\],
bins=\[0, 10, 50, float('inf')\],
labels=\['Low', 'Medium', 'High'\])
print(df\[\['Fare','FareCategory'\]\].head(10))

Heart Disease — missing values, one-hot, modelcleaning

import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

df = pd.read_csv('heart.csv')

# a. Fill missing values

df\['chol'\].fillna(df\['chol'\].median(), inplace=True)
df\['restecg'\].fillna(df\['restecg'\].mode()\[0\], inplace=True)
df\['thal'\].fillna(df\['thal'\].mode()\[0\], inplace=True)

# b. One-hot encoding

df = pd.get_dummies(df, columns=\['sex','cp','thal'\])

# c. Age group

def age_group(age):
if age < 40: return 'young'
elif age < 60: return 'middle-aged'
else: return 'elderly'
df\['AgeGroup'\] = df\['age'\].apply(age_group)

# d. Normalize

scaler = MinMaxScaler()
df\[\['chol','thalach','oldpeak'\]\] = scaler.fit_transform(
df\[\['chol','thalach','oldpeak'\]\])

# e. Build classification model

X = df.drop(columns=\['target','AgeGroup'\])
y = df\['target'\]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = RandomForestClassifier()
model.fit(X_train, y_train)
print(classification_report(y_test, model.predict(X_test)))

Students performance — impute, bucket, label encodecleaning

import pandas as pd
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('StudentsPerformance.csv')

# a. Check and impute missing scores

print(df.isnull().sum())
for col in \['math score','reading score','writing score'\]:
df\[col\].fillna(df\[col\].mean(), inplace=True)

# b. Average score column

df\['AverageScore'\] = df\[\['math score','reading score',
'writing score'\]\].mean(axis=1)

# c. Performance bands

def band(score):
if score >= 80: return 'Excellent'
elif score >= 50: return 'Average'
else: return 'Poor'
df\['PerformanceBand'\] = df\['AverageScore'\].apply(band)

# d. Check duplicates

print(df.duplicated().sum())
df.drop_duplicates(inplace=True)

# e. Label encoding

le = LabelEncoder()
for col in \['gender','lunch','test preparation course'\]:
df\[col+'\_enc'\] = le.fit_transform(df\[col\])

print(df.head())

Patient / employee datasets — merge, group, standardizecleaning

import pandas as pd

patients = pd.read_csv('patients.csv')
visits = pd.read_csv('visits.csv')

# a. Fill/drop missing

patients\['diagnosis'\].fillna('Unknown', inplace=True)
patients.dropna(subset=\['age'\], inplace=True)

# b. Standardize gender values

patients\['gender'\] = patients\['gender'\].replace({
'M':'Male','F':'Female','m':'Male','f':'Female'
})

# c. Merge patient info with visits

merged = pd.merge(patients, visits, on='PatientID', how='inner')

# d. Group: total visits + unique diagnoses per patient

summary = merged.groupby('PatientID').agg(
total_visits=('VisitID','count'),
unique_diagnoses=('diagnosis','nunique')
).reset_index()

# e. Fix out-of-range age

merged = merged\[merged\['age'\] <= 120\]
print(summary)

0 of 2 reviewed

Matplotlib + Seaborn — Toyota, Airquality plotsviz

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Toyota.csv')
df.dropna(inplace=True)

# a. Scatter plot — Age vs Price

plt.figure(figsize=(8,5))
plt.scatter(df\['Age'\], df\['Price'\], alpha=0.5, color='steelblue')
plt.xlabel('Age (years)')
plt.ylabel('Price (€)')
plt.title('Car Age vs Price')
plt.show()

# OR with seaborn

sns.scatterplot(data=df, x='Age', y='Price', hue='FuelType')
plt.show()

# b. Histogram — KM distribution

plt.figure(figsize=(7,4))
plt.hist(df\['KM'\], bins=30, edgecolor='black', color='coral')
plt.xlabel('Kilometers Driven')
plt.title('Distribution of KM')
plt.show()

# c. Bar plot — FuelType count

fuel_counts = df\['FuelType'\].value_counts()
plt.figure(figsize=(6,4))
fuel_counts.plot(kind='bar', color=\['green','blue','orange'\])
plt.title('Car Count by Fuel Type')
plt.ylabel('Count')
plt.xticks(rotation=0)
plt.show()

# Heatmap for correlation

plt.figure(figsize=(8,6))
sns.heatmap(df.select_dtypes('number').corr(),
annot=True, fmt='.2f', cmap='coolwarm')
plt.title('Feature Correlation Heatmap')
plt.show()

# Boxplot — distribution

sns.boxplot(data=df\[\['Price','KM','Age'\]\])
plt.title('Boxplot of Key Features')
plt.show()

Tableau — 7 chart types theory + what to say in oraltableau

7 visualization types — exam answers:

**1D Linear:** Bar chart, histogram. Single dimension. Shows counts, comparisons, distributions. Use for: FuelType count, score distribution.  
**2D Planar:** Scatter plot, map. Two continuous dimensions. Use for: Age vs Price, geographic sales map.  
**3D Volumetric:** 3D surface, 3D scatter. Adds depth/z-axis. Use sparingly — hard to read. Use for: price vs KM vs age in 3D.  
**Temporal:** Line chart, area chart. X-axis is time. Use for: monthly sales, yearly profit trend.  
**Multidimensional:** Parallel coordinates, radar/spider chart, bubble chart. Shows 3+ variables. Use for: student performance across math/reading/writing.  
**Tree/Hierarchical:** Treemap, sunburst. Shows part-to-whole within hierarchy. Use for: sales by Category → Sub-Category.  
**Network:** Force-directed graph, node-link diagram. Shows connections. Use for: social networks, route maps.

Steps to create in Tableau:

Connect to data → drag dimension to Columns shelf → drag measure to Rows shelf → select chart type from Show Me → add Color/Size marks → apply filters → add title → export or add to dashboard.

0 of 1 reviewed

All 3 normalization methods — code for every type askednormalization

import pandas as pd
import numpy as np

df = pd.read_csv('Toyota.csv')
df.dropna(inplace=True)

# 1. Min-Max normalization (0 to 1)

def minmax(col):
return (col - col.min()) / (col.max() - col.min())

df\['HP_minmax'\] = minmax(df\['HP'\])

# Using sklearn

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
df\['Price_minmax'\] = scaler.fit_transform(df\[\['Price'\]\])

# 2. Z-score standardization (mean=0, std=1)

def zscore(col):
return (col - col.mean()) / col.std()

df\['Price_zscore'\] = zscore(df\['Price'\])

# Using sklearn

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
df\['Price_zscore2'\] = sc.fit_transform(df\[\['Price'\]\])

# 3. Decimal scaling

def decimal_scaling(col):
j = len(str(int(col.abs().max()))) # num digits in max value
return col / (10 \*\* j)

df\['Price_decimal'\] = decimal_scaling(df\['Price'\])

# Verify results

print(df\[\['Price','Price_minmax','Price_zscore',
'Price_decimal'\]\].head())
print("Min-max range:", df\['Price_minmax'\].min(),
"to", df\['Price_minmax'\].max())
print("Z-score mean:", round(df\['Price_zscore'\].mean(), 4),
"std:", round(df\['Price_zscore'\].std(), 4))

From the official FAQ list — tap card to reveal answer, then next.

Next question ↗ Reveal / Hide

const TABS=\['faq','hadoop','pandas','cleaning','viz','norm','qf'\]; const cnts={hadoop:0,pandas:0,cleaning:0,viz:0,norm:0}; function sw(id){ TABS.forEach(t=>{ document.getElementById(t).classList.remove('active'); document.querySelectorAll('.tab').forEach((el,i)=>{if(TABS\[i\]===t)el.classList.remove('active')}); }); document.getElementById(id).classList.add('active'); document.querySelectorAll('.tab').forEach((el,i)=>{if(TABS\[i\]===id)el.classList.add('active')}); } function tog(card,grp,total){ const body=card.querySelector('.card-body'); const chev=card.querySelector('.chevron'); const open=body.classList.contains('open'); if(!open){ body.classList.add('open');chev.classList.add('open'); if(grp&&cnts\[grp\]!==undefined&&cnts\[grp\]<total){ cnts\[grp\]++; document.getElementById('prog-'+grp).textContent=cnts\[grp\]+' of '+total+' reviewed'; document.getElementById('bar-'+grp).style.width=Math.round((cnts\[grp\]/total)\*100)+'%'; } } else {body.classList.remove('open');chev.classList.remove('open');} } function filterFAQ(q){ const val=q.toLowerCase(); document.querySelectorAll('#faq-list .card').forEach(c=>{ const txt=(c.dataset.text||'')+(c.querySelector('.card-title')||{textContent:''}).textContent; c.style.display=txt.toLowerCase().includes(val)?'block':'none'; }); } const QF=\[ \["What does jps command show?","Lists all running Java processes — used to verify Hadoop daemons: NameNode, DataNode, ResourceManager, NodeManager, SecondaryNameNode."\], \["What is Secondary NameNode?","Periodically merges FSImage and EditLog to reduce NameNode restart time. NOT a backup NameNode — if NameNode fails, SNN cannot take over."\], \["HDFS default block size and replication?","Block size: 128MB. Replication factor: 3 (stored on 3 different DataNodes)."\], \["What is Hive metastore?","A relational database (Derby/MySQL) that stores Hive table metadata — schema, column names, data types, partition info, and HDFS locations."\], \["df.loc\[\] vs df.iloc\[\]?","loc uses label-based indexing (row/column names). iloc uses integer position-based indexing (0-indexed numbers)."\], \["What is pd.melt()?","Converts wide format (one column per variable) to long format (one row per observation). id_vars stay fixed, all other columns become rows."\], \["What is pivot_table() vs pivot()?","pivot() requires unique index-column combinations. pivot_table() handles duplicates by aggregating (default: mean). pivot_table is more powerful and flexible."\], \["Min-Max formula?","x' = (x - min) / (max - min). Scales to \[0,1\]. Sensitive to outliers."\], \["Z-score formula?","x' = (x - mean) / std_dev. Output has mean=0, std=1. Works well for normally distributed data."\], \["Decimal scaling formula?","x' = x / 10^j where j = number of digits in max(|x|). E.g. max=4521 → j=4 → divide by 10000."\], \["What is one-hot encoding?","Converts categorical column into N binary columns (one per category). Use pd.get_dummies() or sklearn OneHotEncoder. Avoids imposing ordinal relationship."\], \["Label encoding vs one-hot?","Label encoding assigns integers (0,1,2...) — implies order, bad for nominal categories. One-hot creates binary columns — no implied order. Use label encoding for ordinal data (Low/Med/High)."\], \["What is groupby()?","Groups DataFrame by one or more columns, then applies aggregation functions (sum, mean, count, nunique) to each group. Returns a GroupBy object."\], \["CAP theorem in one line?","A distributed system can guarantee only 2 of: Consistency, Availability, Partition tolerance — since partitions always occur, choose CA or CP or AP."\], \["What is data integration?","Combining data from multiple heterogeneous sources into a unified view. Challenges: schema conflicts, duplicate entities, different data formats."\], \["seaborn pairplot purpose?","Shows scatter plots for every pair of numeric features + histograms on diagonal. Quick way to spot correlations and distributions across all features."\], \["What is mrjob?","Python library to write Hadoop MapReduce jobs in Python using class-based mapper/reducer methods, without writing Java."\], \["4 Vs as processing challenges?","Volume → storage and processing capacity. Velocity → need real-time/near-real-time systems. Variety → data integration and schema flexibility. Veracity → data quality and trust issues."\], \["Difference: HBase vs Hive?","HBase: NoSQL, real-time random read/write, row-key based, no SQL. Hive: SQL-like batch analytics on HDFS, no real-time writes, good for structured queries."\], \["What is data transformation?","Converting data into appropriate forms: normalization, aggregation, encoding, binning (pd.cut), log transformation, creating derived features."\], \]; let qfIdx=0, qfFlip=false; function renderQF(){ const q=QF\[qfIdx\]; document.getElementById('qf-count').textContent=(qfIdx+1)+' / '+QF.length; document.getElementById('qf-card').innerHTML=\`<div class="qf-card" onclick="flipQF()"> <div class="qf-q">${q\[0\]}</div> <div class="qf-a" id="qfa" style="display:${qfFlip?'block':'none'}">${q\[1\]}</div> <div class="qf-hint">${qfFlip?'answer shown — tap to hide':'tap to reveal answer'}</div> </div>\`; } function flipQF(){ qfFlip=!qfFlip; renderQF(); } function nextQF(){ qfIdx=(qfIdx+1)%QF.length;qfFlip=false;renderQF(); } renderQF();
