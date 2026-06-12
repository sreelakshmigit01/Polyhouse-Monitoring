import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# ==========================================
# Create figures folder if it doesn't exist
# ==========================================

Path("reports/figures").mkdir(
    parents=True,
    exist_ok=True
)

# ==========================================
# Load cleaned dataset
# ==========================================

df = pd.read_parquet(
    "data/interim/02_cleaned_1000.parquet"
)

print("=" * 50)
print("DATASET INFORMATION")
print("=" * 50)

print("Rows :", len(df))
print("Columns :", len(df.columns))

# ==========================================
# Features for correlation analysis
# ==========================================

features = [
    "temperature_c",
    "humidity_pct",
    "co2_ppm",
    "yield_kg"
]

# ==========================================
# Correlation Heatmap
# ==========================================

corr_matrix = df[features].corr()

fig, ax = plt.subplots(figsize=(7, 6))

im = ax.imshow(
    corr_matrix,
    cmap="coolwarm",
    vmin=-1,
    vmax=1
)

ax.set_xticks(range(len(features)))
ax.set_xticklabels(
    features,
    rotation=45,
    ha="right"
)

ax.set_yticks(range(len(features)))
ax.set_yticklabels(features)

fig.colorbar(
    im,
    ax=ax,
    label="Pearson Correlation"
)

ax.set_title(
    "Correlation Heatmap (1000 Row Dataset)"
)

plt.tight_layout()

plt.savefig(
    "reports/figures/corr_heatmap_1000.png",
    dpi=150,
    bbox_inches="tight"
)

plt.close()

print("Heatmap saved successfully")

# ==========================================
# Scatter Plots
# ==========================================

fig, axes = plt.subplots(
    1,
    3,
    figsize=(15, 5)
)

# ------------------------------------------
# Humidity vs Yield
# ------------------------------------------

axes[0].scatter(
    df["humidity_pct"],
    df["yield_kg"],
    alpha=0.5,
    s=15
)

axes[0].set_title(
    "Humidity vs Yield"
)

axes[0].set_xlabel(
    "Humidity (%)"
)

axes[0].set_ylabel(
    "Yield (kg)"
)

# ------------------------------------------
# Temperature vs Yield
# ------------------------------------------

axes[1].scatter(
    df["temperature_c"],
    df["yield_kg"],
    alpha=0.5,
    s=15
)

axes[1].set_title(
    "Temperature vs Yield"
)

axes[1].set_xlabel(
    "Temperature (°C)"
)

axes[1].set_ylabel(
    "Yield (kg)"
)

# ------------------------------------------
# CO2 vs Yield
# ------------------------------------------

axes[2].scatter(
    df["co2_ppm"],
    df["yield_kg"],
    alpha=0.5,
    s=15
)

axes[2].set_title(
    "CO₂ vs Yield"
)

axes[2].set_xlabel(
    "CO₂ (ppm)"
)

axes[2].set_ylabel(
    "Yield (kg)"
)

plt.tight_layout()

plt.savefig(
    "reports/figures/scatter_yield_1000.png",
    dpi=150,
    bbox_inches="tight"
)

plt.close()

print("Scatter plots saved successfully")

print("\nEDA completed successfully")
print("\nGenerated files:")
print("1. reports/figures/corr_heatmap_1000.png")
print("2. reports/figures/scatter_yield_1000.png")