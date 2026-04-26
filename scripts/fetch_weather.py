import os
import json
import requests
from datetime import datetime
from pathlib import Path

API_KEY = os.getenv("OPENWEATHER_API_KEY")

CITIES = ["Yalova,TR", "Istanbul,TR", "Ankara,TR", "Bursa,TR", "Kocaeli,TR"]

if not API_KEY:
    raise ValueError("OPENWEATHER_API_KEY bulunamadı.")

today = datetime.utcnow().strftime("%Y-%m-%d")
output_dir = Path("data/weather")
output_dir.mkdir(parents=True, exist_ok=True)

all_data = []

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

file_path = output_dir / f"{today}.json"

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(all_data, f, ensure_ascii=False, indent=2)

print(f"Weather data saved: {file_path}")
