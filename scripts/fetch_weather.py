import os
import json
import csv
import requests
from datetime import datetime
from pathlib import Path

API_KEY = os.getenv("OPENWEATHER_API_KEY")

CITIES = ["Yalova,TR", "Istanbul,TR", "Ankara,TR", "Bursa,TR", "Kocaeli,TR"]

if not API_KEY:
    raise ValueError("OPENWEATHER_API_KEY bulunamadı.")

today = datetime.utcnow().strftime("%Y-%m-%d")

json_dir = Path("data/weather/json")
csv_dir = Path("data/weather/csv")
reports_dir = Path("reports")

json_dir.mkdir(parents=True, exist_ok=True)
csv_dir.mkdir(parents=True, exist_ok=True)
reports_dir.mkdir(parents=True, exist_ok=True)

all_data = []
rows = []

for city in CITIES:
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",
        "lang": "tr"
    }

    response = requests.get(url, params=params, timeout=20)
    response.raise_for_status()

    data = response.json()
    all_data.append(data)

    rows.append({
        "date": today,
        "city": data["name"],
        "country": data["sys"]["country"],
        "temperature": data["main"]["temp"],
        "feels_like": data["main"]["feels_like"],
        "humidity": data["main"]["humidity"],
        "pressure": data["main"]["pressure"],
        "weather": data["weather"][0]["description"],
        "wind_speed": data["wind"]["speed"]
    })

json_path = json_dir / f"{today}.json"
csv_path = csv_dir / f"{today}.csv"

with open(json_path, "w", encoding="utf-8") as f:
    json.dump(all_data, f, ensure_ascii=False, indent=2)

with open(csv_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)

print(f"JSON saved: {json_path}")
print(f"CSV saved: {csv_path}")
