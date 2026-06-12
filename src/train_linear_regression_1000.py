from pathlib import Path
import json
import numpy as np
import pandas as pd
import joblib

from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

# Create folders if needed
Path("models").mkdir(exist_ok=True)
Path("reports").mkdir(exist_ok=True)

# Load datasets
X_train = pd.read_parquet(
    "data/processed/X_train_1000.parquet"
)

X_test = pd.read_parquet(
    "data/processed/X_test_1000.parquet"
)

y_train = pd.read_parquet(
    "data/processed/y_train_1000.parquet"
).squeeze()

y_test = pd.read_parquet(
    "data/processed/y_test_1000.parquet"
).squeeze()

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
pred_test = model.predict(X_test)

# Metrics
mae = mean_absolute_error(y_test, pred_test)
rmse = np.sqrt(mean_squared_error(y_test, pred_test))
r2 = r2_score(y_test, pred_test)

print("\nLINEAR REGRESSION RESULTS")
print("=" * 40)
print(f"MAE  : {mae:.3f}")
print(f"RMSE : {rmse:.3f}")
print(f"R²   : {r2:.3f}")

print("\nCOEFFICIENTS")
for feature, coef in zip(X_train.columns, model.coef_):
    print(f"{feature}: {coef:.4f}")

# Save model
joblib.dump(
    model,
    "models/linear_regression_1000.joblib"
)

# Save metrics
metrics = {
    "mae": float(mae),
    "rmse": float(rmse),
    "r2": float(r2)
}

with open(
    "reports/metrics_linear_1000.json",
    "w"
) as f:
    json.dump(metrics, f, indent=4)

print("\nModel and metrics saved successfully.")