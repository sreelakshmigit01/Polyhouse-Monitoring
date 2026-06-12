# Polyhouse Monitoring Project

## Problem Statement

This project focuses on monitoring polyhouse environmental conditions such as temperature, humidity, CO₂ levels, and crop yield. The objective is to build a reproducible data science workflow for collecting, processing, analyzing, and modeling sensor data for agritech applications.

## Folder Structure

project/
│
├── data/
│   ├── raw/
│   ├── interim/
│   └── processed/
├── docs/
├── reports/
│   └── figures/
├── src/
├── models/
├── smoke_test.py
├── requirements.txt
├── .gitignore
└── README.md

## Environment Setup

### 1. Create a Virtual Environment

python -m venv myenv

### 2. Activate the Environment

myenv\Scripts\activate

### 3. Install Dependencies

pip install -r requirements.txt

### 4. Run the Smoke Test

python smoke_test.py

## Dependencies

The project dependencies are listed in requirements.txt.

## Version Control

Git is used for version control. The repository is hosted on GitHub and all project changes are tracked through commits.

# Dataset Columns

### timestamp

Date and time when sensor reading was recorded.

### temperature_c

Polyhouse temperature in degrees Celsius.

### humidity_pct

Relative humidity percentage.

### co2_ppm

Carbon dioxide concentration in parts per million.

### yield_kg

Harvested mushroom yield in kilograms.

# Data Cleaning

Cleaning operations performed:

* Missing value handling
* Data validation checks
* Yield validation
* Duplicate removal
* Timestamp parsing
* Data type correction

## Dataset Summary

### Raw Dataset

Rows: 1005

### Cleaned Dataset

Rows: 979

### Date Range

Start: 2024-01-01 00:00:00

End: 2024-02-11 15:00:00

## Output Files

data/interim/01_loaded_1000.parquet

data/interim/02_cleaned_1000.parquet

docs/cleaning_log_1000.md

reports/data_quality_1000.md

# Exploratory Data Analysis (EDA)

EDA was performed to analyze:

* Feature distributions
* Correlation between variables
* Yield relationships
* Potential anomalies

## Generated Visualizations

reports/figures/corr_heatmap_1000.png

reports/figures/scatter_yield_1000.png

## EDA Notes

reports/figures/ were generated using Matplotlib and Pandas to understand relationships among environmental variables and crop yield.

# Feature Engineering

## Features Used

1. temperature_c
2. humidity_pct
3. co2_ppm

## Target

yield_kg

## Scaler

MinMaxScaler

## Outputs

data/processed/features_1000.parquet

models/minmax_scaler_1000.joblib

# Train/Test Split

## Split Method

A chronological 80/20 train-test split was used to preserve temporal order and prevent future information from influencing model training.

## Features

* temperature_c
* humidity_pct
* co2_ppm

## Target

* yield_kg

## Dataset Size

* Total Rows: 979
* Training Rows: 783
* Testing Rows: 196

## Date Range

* Training Period: Earliest records from cleaned dataset
* Testing Period: Most recent 20% of records

## Scaling

MinMaxScaler was fitted on the training data only and then used to transform both training and testing datasets. This prevents data leakage from the test set.

## Saved Scaler

models/minmax_scaler_train_1000.joblib

## Saved Split Artifacts

data/processed/X_train_1000.parquet

data/processed/X_test_1000.parquet

data/processed/y_train_1000.parquet

data/processed/y_test_1000.parquet

# Linear Regression Baseline Model

A Linear Regression model was trained as an interpretable baseline model for yield prediction.

## Model Features

* temperature_c
* humidity_pct
* co2_ppm

## Saved Model

models/linear_regression_1000.joblib

## Model Performance

| Metric | Value    |
| ------ | -------- |
| MAE    | 0.206 kg |
| RMSE   | 0.253 kg |
| R²     | 0.870    |

## Coefficients

| Feature       | Coefficient |
| ------------- | ----------- |
| temperature_c | 2.8370      |
| humidity_pct  | 1.7381      |
| co2_ppm       | -2.3961     |

## Interpretation

* Temperature shows a positive influence on yield.
* Humidity shows a positive influence on yield.
* CO₂ shows a negative influence on yield in the scaled feature space.
* Linear Regression provides a strong and interpretable baseline model.

## Generated Reports

reports/metrics_linear_1000.json

reports/coefficient_interpretation_1000.md

reports/baseline_evaluation_1000.md

# Model Diagnostics

Residual analysis was performed to evaluate prediction errors.

## Generated Figure

reports/figures/residuals_linear_1000.png

## Findings

* Residuals are centered around zero.
* No major nonlinear pattern observed.
* No significant heteroscedasticity detected.
* A few isolated larger residuals were present.

## Diagnostic Report

reports/linear_diagnostics_1000.md

## Recommendation

Linear Regression performs well as a baseline model. More advanced models such as Random Forest Regression can be explored to capture nonlinear relationships and potentially improve predictive performance.

# Models Directory

models/

├── linear_regression_1000.joblib

├── minmax_scaler_1000.joblib

└── minmax_scaler_train_1000.joblib

# Reports Directory

reports/

├── data_quality_1000.md

├── baseline_evaluation_1000.md

├── coefficient_interpretation_1000.md

├── linear_diagnostics_1000.md

├── metrics_linear_1000.json

└── figures/

    ├── corr_heatmap_1000.png

    ├── scatter_yield_1000.png

    └── residuals_linear_1000.png

# Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-Learn
* Joblib
* PyArrow
* Git
* GitHub

# Future Scope

* Random Forest Regression
* Hyperparameter tuning
* Streamlit dashboard development
* Real-time sensor monitoring
* Time-series forecasting
