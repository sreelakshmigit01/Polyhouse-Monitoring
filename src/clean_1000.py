# src/clean_1000.py
import pandas as pd

# -------------------------
# Load Data
# -------------------------
df = pd.read_parquet("data/interim/01_loaded_1000.parquet")

print("=" * 50)
print("MISSING VALUE REPORT (RAW)")
print("=" * 50)
print(df.isna().sum())

print("\nRaw descriptive stats:")
print(df[["temperature_c", "humidity_pct", "co2_ppm", "yield_kg"]].describe())

rows_before = len(df)

# -------------------------
# Step 1: Remove Invalid Sensor Ranges FIRST
# (before median fill so median is from clean data)
# Realistic Polyhouse Ranges
# Raw data confirmed: temp had -15 & 55, humidity had -10 & 120,
# co2 had 6000 spike — all caught by these bounds
# -------------------------
df = df[
    (
        (df["temperature_c"] >= 15) &
        (df["temperature_c"] <= 35)
    ) | df["temperature_c"].isna()
].copy()

df = df[
    (
        (df["humidity_pct"] >= 70) &
        (df["humidity_pct"] <= 100)
    ) | df["humidity_pct"].isna()
].copy()

df = df[
    (
        (df["co2_ppm"] >= 300) &
        (df["co2_ppm"] <= 2000)
    ) | df["co2_ppm"].isna()
].copy()

rows_after_range = len(df)

# -------------------------
# Step 2: Fill Sensor Missing Values
# Median is now computed on range-filtered clean data
# -------------------------
sensor_cols = [
    "temperature_c",
    "humidity_pct",
    "co2_ppm"
]

print("\n" + "=" * 50)
print("MEDIAN FILL VALUES (from clean data)")
print("=" * 50)
for col in sensor_cols:
    median_value = df[col].median()
    print(f"  {col}: {median_value:.4f}")
    df[col] = df[col].fillna(median_value)

# -------------------------
# Step 3: Remove Missing Target
# -------------------------
df = df.dropna(subset=["yield_kg"])
rows_after_target = len(df)

# -------------------------
# Step 4: Remove Invalid yield_kg Values
# Raw data confirmed: -4.0 kg (row 300) and 40.0 kg outlier
# Normal yield band is ~15-20 kg based on describe() output
# -------------------------
YIELD_MIN = 0
YIELD_MAX = 25  # kg — tightened based on raw data (mean=17, std=1.35)

df = df[
    (df["yield_kg"] >= YIELD_MIN) &
    (df["yield_kg"] <= YIELD_MAX)
].copy()

rows_after_yield_range = len(df)

# -------------------------
# Step 5: IQR Outlier Removal on yield_kg
# Catches any remaining statistical outliers within valid range
# -------------------------
Q1 = df["yield_kg"].quantile(0.25)
Q3 = df["yield_kg"].quantile(0.75)
IQR = Q3 - Q1
lower_fence = Q1 - 1.5 * IQR
upper_fence = Q3 + 1.5 * IQR

print("\n" + "=" * 50)
print("IQR OUTLIER FENCES (yield_kg)")
print("=" * 50)
print(f"  Q1         : {Q1:.4f}")
print(f"  Q3         : {Q3:.4f}")
print(f"  IQR        : {IQR:.4f}")
print(f"  Lower fence: {lower_fence:.4f}")
print(f"  Upper fence: {upper_fence:.4f}")

df = df[
    (df["yield_kg"] >= lower_fence) &
    (df["yield_kg"] <= upper_fence)
].copy()

rows_after_iqr = len(df)

# -------------------------
# Step 6: Remove Duplicate Timestamps
# -------------------------
df = df.drop_duplicates(
    subset=["timestamp"],
    keep="last"
)
rows_after_duplicates = len(df)

# -------------------------
# Step 7: CO2 Diagnostic
# After cleaning the 6000 ppm spike, correlation should
# be near zero or weakly negative (plausible)
# -------------------------
co2_yield_corr = df["co2_ppm"].corr(df["yield_kg"])
print("\n" + "=" * 50)
print("CO2 DIAGNOSTIC")
print("=" * 50)
print(f"  co2_ppm vs yield_kg Pearson correlation: {co2_yield_corr:.4f}")
if co2_yield_corr < -0.3:
    print(
        "  ⚠️  WARNING: Strong negative CO2-yield correlation detected.\n"
        "  Check raw data for remaining co2_ppm anomalies or\n"
        "  a possible column misalignment in the loading step."
    )
else:
    print("  ✅ CO2-yield correlation looks plausible.")

# -------------------------
# Save Clean Dataset
# -------------------------
df.to_parquet(
    "data/interim/02_cleaned_1000.parquet",
    index=False
)

# -------------------------
# Cleaning Summary
# -------------------------
print("\n" + "=" * 50)
print("CLEANING SUMMARY")
print("=" * 50)
print(f"Rows before cleaning          : {rows_before}")
print(f"Rows after sensor range filter: {rows_after_range}")
print(f"Rows after target null drop   : {rows_after_target}")
print(f"Rows after yield range filter : {rows_after_yield_range}")
print(f"Rows after IQR outlier removal: {rows_after_iqr}")
print(f"Rows after duplicate removal  : {rows_after_duplicates}")
print(f"\nFinal Shape: {df.shape}")

# -------------------------
# Final Validation
# -------------------------
print("\n" + "=" * 50)
print("FINAL VALIDATION CHECK")
print("=" * 50)
print(f"Temperature : {df['temperature_c'].min():.2f} to {df['temperature_c'].max():.2f} °C")
print(f"Humidity    : {df['humidity_pct'].min():.2f} to {df['humidity_pct'].max():.2f} %")
print(f"CO2         : {df['co2_ppm'].min():.2f} to {df['co2_ppm'].max():.2f} ppm")
print(f"Yield       : {df['yield_kg'].min():.2f} to {df['yield_kg'].max():.2f} kg")
print(f"\nRemaining nulls:\n{df.isna().sum()}")