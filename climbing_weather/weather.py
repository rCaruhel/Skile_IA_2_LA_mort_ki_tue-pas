#!/usr/bin/env python3
import argparse
import json
import requests
from datetime import datetime

OPEN_METEO_URL = "https://api.open-meteo.com/v1/forecast"

def get_best_time_to_climb(lat: float, lon: float, is_indoor: bool):
    if is_indoor:
        return [{"message": "Indoor spot, no weather constraints. Go anytime!"}]

    params = {
        "latitude": lat,
        "longitude": lon,
        "hourly": ["temperature_2m", "precipitation"],
        "timezone": "auto",
        "forecast_days": 3
    }
    
    try:
        response = requests.get(OPEN_METEO_URL, params=params)
        response.raise_for_status()
        forecast = response.json()
        
        hourly = forecast.get("hourly", {})
        times = hourly.get("time", [])
        temps = hourly.get("temperature_2m", [])
        precips = hourly.get("precipitation", [])
        
        good_slots = []
        for i in range(len(times)):
            dt = datetime.fromisoformat(times[i])
            if 8 <= dt.hour <= 19:
                recent_rain = False
                if i >= 2:
                    recent_rain = sum(precips[i-2:i+1]) > 0
                
                if 5 <= temps[i] <= 25 and not recent_rain:
                    good_slots.append({
                        "time": times[i],
                        "temp_C": temps[i],
                        "precip_mm": precips[i]
                    })
        return good_slots[:5]
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find best time to climb based on weather.")
    parser.add_argument("--lat", type=float, required=True)
    parser.add_argument("--lon", type=float, required=True)
    parser.add_argument("--indoor", action="store_true", help="Set if the spot is indoor")
    args = parser.parse_args()
    
    result = get_best_time_to_climb(args.lat, args.lon, args.indoor)
    print(json.dumps(result, ensure_ascii=False))
