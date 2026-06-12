from pathlib import Path
import pandas as pd

# Load cleaned dataset

df = pd.read_parquet("data/interim/02_cleaned_1000.parquet")

# Summary statistics

summary = df[
[
"temperature_c",
"humidity_pct",
"co2_ppm",
"yield_kg"
]
].describe().T

# Coefficient of Variation

summary["cv"] = summary["std"] / summary["mean"]

# Round values

summary = summary.round(2)

# Dataset information

rows = len(df)
start_date = df["timestamp"].min()
end_date = df["timestamp"].max()

# Sampling frequency

sampling_frequency = (
df["timestamp"]
.sort_values()
.diff()
.mode()[0]
)

# Yield analysis

mean_yield = df["yield_kg"].mean()
median_yield = df["yield_kg"].median()

if mean_yield > median_yield:
    yield_insight = (
    "Mean yield exceeds median yield, suggesting a few high-yield days increased the average."
    )
else:
    yield_insight = (
    "Mean and median yield are similar, indicating limited skew in yield."
    )

# Humidity analysis

humidity_mean = df["humidity_pct"].mean()
humidity_min = df["humidity_pct"].min()
humidity_max = df["humidity_pct"].max()

humidity_insight = (
f"Humidity averaged {humidity_mean:.2f}%, "
f"with values ranging from {humidity_min:.2f}% "
f"to {humidity_max:.2f}%."
)

# Create report

report = []

report.append("# Polyhouse Data Quality Report\n")

report.append("## Executive Summary\n")
report.append(
f"The dataset contains {rows} observations. "
f"Average yield was {mean_yield:.2f} kg/day.\n"
)

report.append("## Dataset Overview\n")
report.append(f"Rows: {rows}")
report.append(f"Date Range: {start_date} → {end_date}")
report.append(f"Sampling Frequency: {sampling_frequency}\n")

report.append("## Summary Statistics\n")
report.append(summary.to_markdown())

report.append("\n## Key Insights\n")
report.append(f"- {yield_insight}")
report.append(f"- {humidity_insight}")

# Convert to text

report_content = "\n".join(report)

# Create reports folder

Path("reports").mkdir(exist_ok=True)

# Save report

Path(
"reports/data_quality_1000.md"
).write_text(
report_content,
encoding="utf-8"
)

print("Data quality report generated successfully.")
print("Saved to reports/data_quality_1000.md")
