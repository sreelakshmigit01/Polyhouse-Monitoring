from pathlib import Path
import pandas as pd

df = pd.read_parquet("data/interim/02_cleaned.parquet")
summary = df[
    [
        "temperature_c",
        "humidity_pct",
        "co2_ppm",
        "yield_kg"
    ]
].describe().T
summary["cv"] = summary["std"] / summary["mean"]
summary = summary.round(2)
rows = len(df)
start_date = df["timestamp"].min()
end_date = df["timestamp"].max()
sampling_frequency = (
    df["timestamp"]
    .sort_values()
    .diff()
    .mode()[0]
)
mean_yield = df["yield_kg"].mean()
median_yield = df["yield_kg"].median()
if mean_yield > median_yield:
    yield_insight = (
        "Mean yield exceeds median yield, suggesting a few high-yield days increased the average."
    )
else:
    yield_insight = (
        "Mean and median yield are similar, indicating little skew in yield."
    )
humidity_mean = df["humidity_pct"].mean()
if 85 <= humidity_mean <= 90:
    humidity_insight = (
        "Humidity remained within the recommended cultivation range of 85–90%."
    )
else:
    humidity_insight = (
        "Humidity deviated from the recommended cultivation range."
    )
report = []
report.append("# Polyhouse Data Quality Report\n")
report.append("## Executive Summary\n")

report.append(
    f"The dataset contains {rows} observations."
)

report.append(
    f" Average yield was {mean_yield:.2f} kg/day.\n"
)
report.append("## Dataset Overview\n")

report.append(f"Rows: {rows}")

report.append(
    f"Date Range: {start_date} → {end_date}"
)

report.append(
    f"Sampling Frequency: {sampling_frequency}\n"
)
report.append("## Summary Statistics\n")

report.append(summary.to_markdown())
report.append("\n## Key Insights\n")

report.append(f"- {yield_insight}")

report.append(f"- {humidity_insight}")
report_content = "\n".join(report)
Path("reports").mkdir(exist_ok=True)
Path(
    "reports/data_quality.md"
).write_text(
    report_content,
    encoding="utf-8"
)