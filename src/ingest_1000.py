import pandas as pd
from pathlib import Path

# -----------------------------
# File Paths
# -----------------------------
RAW = Path("data/raw/polyhousesensors1.csv")

INTERIM = Path("data/interim")
INTERIM.mkdir(parents=True, exist_ok=True)

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv(
    RAW,
    parse_dates=["timestamp"]
)

# -----------------------------
# Verification
# -----------------------------
print("\n===== SHAPE =====")
print(df.shape)

print("\n===== COLUMN NAMES =====")
print(df.columns)

print("\n===== DATA TYPES =====")
print(df.dtypes)

print("\n===== FIRST 5 ROWS =====")
print(df.head())

print("\n===== INFO =====")
df.info()

print("\n===== DESCRIBE =====")
print(df.describe())

print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

print("\n===== DUPLICATE ROWS =====")
print(df.duplicated().sum())

# -----------------------------
# Save Interim Snapshot
# -----------------------------
output_file = INTERIM / "01_loaded_1000.parquet"

df.to_parquet(
    output_file,
    index=False
)

print("\n===== SNAPSHOT SAVED =====")
print(output_file)