\# Data Cleaning Log



Input File:

01\_loaded.parquet



Cleaning Actions



1\. Generated missing value report.



2\. Applied validity rules:

&nbsp;  - Humidity: 50–100%

&nbsp;  - Temperature: 10–35°C

&nbsp;  - CO₂: 400–2000 ppm



3\. Forward-filled sensor columns:

&nbsp;  - temperature\_c

&nbsp;  - humidity\_pct

&nbsp;  - co2\_ppm



4\. Forward-fill limit:

&nbsp;  2 rows



5\. Removed rows with missing yield\_kg.



6\. Removed duplicate timestamps.



Duplicate Handling:

Keep the last timestamp record.



Output File:

02\_cleaned.parquet



Verification:

yield\_kg null count = 0

