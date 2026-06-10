import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import joblib

df = pd.read_parquet("data/interim/02_cleaned.parquet").sort_values("timestamp")

feature_cols = ["temperature_c", "humidity_pct", "co2_ppm"]

split_idx = int(len(df) * 0.8)

train = df.iloc[:split_idx]
test = df.iloc[split_idx:]

scaler = MinMaxScaler()

X_train = scaler.fit_transform(train[feature_cols])
X_test = scaler.transform(test[feature_cols])

y_train = train["yield_kg"].values
y_test = test["yield_kg"].values

joblib.dump(
    scaler,
    "models/minmax_scaler_train.joblib"
)

# Save train/test artifacts
pd.DataFrame(
    X_train,
    columns=feature_cols
).to_parquet(
    "data/processed/X_train.parquet",
    index=False
)

pd.DataFrame(
    X_test,
    columns=feature_cols
).to_parquet(
    "data/processed/X_test.parquet",
    index=False
)

pd.DataFrame(
    {"yield_kg": y_train}
).to_parquet(
    "data/processed/y_train.parquet",
    index=False
)

pd.DataFrame(
    {"yield_kg": y_test}
).to_parquet(
    "data/processed/y_test.parquet",
    index=False
)

print(f"Train: {train['timestamp'].min()} → {train['timestamp'].max()}")
print(f"Test:  {test['timestamp'].min()} → {test['timestamp'].max()}")

print("Train rows:", len(train))
print("Test rows:", len(test))

print("Split artifacts saved.")