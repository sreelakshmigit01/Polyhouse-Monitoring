# Polyhouse Monitoring Project

## Problem Statement

This project focuses on monitoring polyhouse environmental conditions such as temperature, humidity, CO₂ levels, and crop yield. The objective is to build a reproducible data science workflow for collecting, processing, and analyzing sensor data for agritech applications.

## Folder Structure

project/
│
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
├── src/
├── models/
├── smoke_test.py
├── requirements.txt
├── .gitignore
└── README.md

## Environment Setup

1. Create a virtual environment

   python -m venv myenv

2. Activate the environment

   myenv\Scripts\activate

3. Install dependencies

   pip install -r requirements.txt

4. Run the smoke test

   python smoke_test.py

## Dependencies

The project dependencies are listed in requirements.txt.

## Version Control

Git is used for version control. The repository is hosted on GitHub and all project changes are tracked through commits.

#Dataset Columns

timestamp:
Date and time when sensor reading was recorded.

temperature_c:
Polyhouse temperature in degrees Celsius.

humidity_pct:
Relative humidity percentage.

co2_ppm:
Carbon dioxide concentration in parts per million.

yield_kg:
Harvested mushroom yield in kilograms.


#Feature Engineering

Features Used:
1. temperature_c
2. humidity_pct
3. co2_ppm
4. temp_humid_interaction

Formula:
temp_humid_interaction =
temperature_c × humidity_pct / 100

Target:
yield_kg

Scaler:
MinMaxScaler

Outputs:
data/processed/features.parquet
models/minmax_scaler.joblib