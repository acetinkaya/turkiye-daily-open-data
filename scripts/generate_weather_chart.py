import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

csv_dir = Path("data/weather/csv")
reports_dir = Path("reports")
reports_dir.mkdir(parents=True, exist_ok=True)

latest_csv = sorted(csv_dir.glob("*.csv"))[-1]

df = pd.read_csv(latest_csv)

plt.figure(figsize=(10, 6))
plt.bar(df["city"], df["temperature"])
plt.title("Daily Temperature Values - Türkiye")
plt.xlabel("City")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=30)
plt.tight_layout()

chart_path = reports_dir / "weather_temperature_chart.png"
plt.savefig(chart_path, dpi=150)

print(f"Chart saved: {chart_path}")
