from pathlib import Path

import joblib
import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# CREATE FIGURES FOLDER
# ==========================================

Path("reports/figures").mkdir(
    parents=True,
    exist_ok=True
)

# ==========================================
# LOAD DATA
# ==========================================

X_test = pd.read_parquet(
    "data/processed/X_test_1000.parquet"
)

y_test = pd.read_parquet(
    "data/processed/y_test_1000.parquet"
).squeeze()

# ==========================================
# LOAD MODEL
# ==========================================

model = joblib.load(
    "models/linear_regression_1000.joblib"
)

# ==========================================
# PREDICTIONS
# ==========================================

pred_test = model.predict(X_test)

# ==========================================
# RESIDUALS
# ==========================================

residuals = y_test - pred_test

print("Residuals calculated")

# ==========================================
# CREATE PLOTS
# ==========================================

fig, axes = plt.subplots(
    1,
    2,
    figsize=(10, 4)
)

# Residuals vs Predicted

axes[0].scatter(
    pred_test,
    residuals,
    alpha=0.6
)

axes[0].axhline(
    0,
    color="red",
    linestyle="--"
)

axes[0].set_title(
    "Residuals vs Predicted Yield"
)

axes[0].set_xlabel(
    "Predicted Yield (kg)"
)

axes[0].set_ylabel(
    "Residual (kg)"
)

# Residuals vs Humidity

axes[1].scatter(
    X_test["humidity_pct"],
    residuals,
    alpha=0.6
)

axes[1].axhline(
    0,
    color="red",
    linestyle="--"
)

axes[1].set_title(
    "Residuals vs Humidity"
)

axes[1].set_xlabel(
    "Scaled Humidity"
)

axes[1].set_ylabel(
    "Residual (kg)"
)

plt.tight_layout()

plt.savefig(
    "reports/figures/residuals_linear_1000.png",
    dpi=150
)

plt.show()

print(
    "Figure saved successfully"
)