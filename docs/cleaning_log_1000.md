\# Data Cleaning Log



\## Task 2 – Data Cleaning



\### Input File



\* 01\_loaded\_1000.parquet



\### Dataset Overview



\* Rows before cleaning: 1005

\* Columns: 5



\---



\## Missing Value Report



| Column        | Missing Values |

| ------------- | -------------: |

| timestamp     |              0 |

| temperature\_c |              5 |

| humidity\_pct  |              5 |

| co2\_ppm       |              5 |

| yield\_kg      |              5 |



\---



\## Cleaning Strategy



\### 1. Missing Value Handling



Sensor columns were imputed using median values calculated from valid observations.



Columns imputed:



\* temperature\_c

\* humidity\_pct

\* co2\_ppm



Median values used:



\* temperature\_c = 22.04

\* humidity\_pct = 87.20

\* co2\_ppm = 900



Target values (`yield\_kg`) were not imputed to avoid introducing artificial labels.



Rows with missing target values were removed.



\---



\### 2. Sensor Range Validation



Rows containing impossible sensor readings were removed.



Validation rules:



\* Temperature: 0–50 °C

\* Humidity: 0–100 %

\* CO₂: greater than 0 ppm



Rows after sensor range filtering: \*\*998\*\*



\---



\### 3. Target Cleaning



Rows with missing yield values were removed.



Rows after target null removal: \*\*993\*\*



\---



\### 4. Yield Range Validation



Rows containing unrealistic yield values were removed.



Rows after yield range filtering: \*\*990\*\*



\---



\### 5. IQR Outlier Removal



Interquartile Range (IQR) analysis was used to identify extreme yield outliers.



Yield statistics:



\* Q1 = 16.5225

\* Q3 = 17.5300

\* IQR = 1.0075



Calculated fences:



\* Lower Fence = 15.0113

\* Upper Fence = 19.0413



Rows after IQR outlier removal: \*\*983\*\*



\---



\### 6. Duplicate Handling



Duplicate timestamps were removed.



Rule used:



\* Keep the last occurrence (`keep="last"`)



Rows after duplicate removal: \*\*979\*\*



\---



\## Cleaning Summary



| Step                      | Row Count |

| ------------------------- | --------: |

| Before Cleaning           |      1005 |

| After Sensor Range Filter |       998 |

| After Target Null Drop    |       993 |

| After Yield Range Filter  |       990 |

| After IQR Outlier Removal |       983 |

| After Duplicate Removal   |       979 |



Total rows removed: \*\*26\*\*



Data retained: \*\*979 rows\*\*



\---



\## CO₂ Diagnostic Check



Pearson correlation between CO₂ and yield:



\* Correlation = -0.5044



Observation:



A moderately strong negative relationship was observed between CO₂ concentration and yield in this dataset. This result was retained for analysis and documented for future investigation.



\---



\## Final Validation Check



\### Temperature



17.95 °C to 26.08 °C



\### Humidity



78.20 % to 96.60 %



\### CO₂



658 ppm to 1214 ppm



\### Yield



15.05 kg to 19.02 kg



\---



\## Verification



\* Final dataset shape: \*\*(979, 5)\*\*

\* Null values in temperature\_c: \*\*0\*\*

\* Null values in humidity\_pct: \*\*0\*\*

\* Null values in co2\_ppm: \*\*0\*\*

\* Null values in yield\_kg: \*\*0\*\*



Cleaned dataset successfully exported.



\---



\## Output File



\* 02\_cleaned\_1000.parquet



