import pandas as pd
import numpy as np

np.random.seed(42)

# ==========================================
# Generate 1000 Sensor Records
# ==========================================

n = 1000

timestamps = pd.date_range(
    start="2024-01-01",
    periods=n,
    freq="h"
)

temperature = np.random.normal(
    loc=22,
    scale=1.5,
    size=n
)

humidity = np.random.normal(
    loc=87,
    scale=3,
    size=n
)

co2 = np.random.normal(
    loc=900,
    scale=80,
    size=n
)

# ==========================================
# Yield depends on sensors
# ==========================================

yield_kg = (
    17
    + 0.35 * (temperature - 22)
    + 0.10 * (humidity - 87)
    - 0.005 * (co2 - 900)
    + np.random.normal(0, 0.25, n)
)

df = pd.DataFrame({
    "timestamp": timestamps,
    "temperature_c": temperature,
    "humidity_pct": humidity,
    "co2_ppm": co2,
    "yield_kg": yield_kg
})

# Round values

df["temperature_c"] = df["temperature_c"].round(2)
df["humidity_pct"] = df["humidity_pct"].round(1)
df["co2_ppm"] = df["co2_ppm"].round(0)
df["yield_kg"] = df["yield_kg"].round(2)

# ==========================================
# Add Missing Values
# ==========================================

missing_rows = np.random.choice(
    df.index,
    size=20,
    replace=False
)

df.loc[missing_rows[:5], "temperature_c"] = np.nan
df.loc[missing_rows[5:10], "humidity_pct"] = np.nan
df.loc[missing_rows[10:15], "co2_ppm"] = np.nan
df.loc[missing_rows[15:20], "yield_kg"] = np.nan

# ==========================================
# Rule Violations
# ==========================================

df.loc[50, "humidity_pct"] = 120
df.loc[120, "humidity_pct"] = -10

df.loc[180, "temperature_c"] = -15
df.loc[250, "temperature_c"] = 55

df.loc[300, "yield_kg"] = -4

# ==========================================
# Extreme Outliers
# ==========================================

df.loc[400, "co2_ppm"] = 5000
df.loc[500, "co2_ppm"] = 6000

df.loc[600, "yield_kg"] = 35
df.loc[700, "yield_kg"] = 40

# ==========================================
# Duplicate Rows
# ==========================================

duplicates = df.iloc[[10, 20, 30, 40, 50]]

df = pd.concat(
    [df, duplicates],
    ignore_index=True
)

# ==========================================
# Save CSV
# ==========================================

df.to_csv(
    "polyhousesensors1.csv",
    index=False
)

print("Dataset Generated Successfully")
print("Rows:", len(df))