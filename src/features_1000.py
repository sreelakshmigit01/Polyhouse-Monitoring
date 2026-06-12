import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import joblib

df = pd.read_parquet("data/interim/02_cleaned_1000.parquet").sort_values("timestamp")

df["temp_humid_interaction"] = (
    df["temperature_c"] *
    df["humidity_pct"] / 100
)

feature_cols = [
    "temperature_c",
    "humidity_pct",
    "co2_ppm",
    "temp_humid_interaction"
]

X = df[feature_cols]
y = df["yield_kg"]

scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

joblib.dump(
    scaler,
    "models/minmax_scaler_1000.joblib"
)

processed = pd.DataFrame(
    X_scaled,
    columns=[c + "_scaled" for c in feature_cols]
)

processed["yield_kg"] = y.values

processed.to_parquet(
    "data/processed/features_1000.parquet",
    index=False
)

print("Feature engineering completed.")
print("Processed data saved.")
print("Scaler saved.")