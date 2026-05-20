#!/usr/bin/env python3
import argparse
import json
import requests
import sys
sys.stdout.reconfigure(encoding='utf-8')

OVERPASS_URL = "http://overpass-api.de/api/interpreter"

def find_climbing_spots(lat: float, lon: float, radius: int):
    query = f"""
    [out:json][timeout:25];
    (
      node["sport"="climbing"](around:{radius},{lat},{lon});
      way["sport"="climbing"](around:{radius},{lat},{lon});
      relation["sport"="climbing"](around:{radius},{lat},{lon});
    );
    out center;
    """
    try:
        headers = {"User-Agent": "Skile_IA_Climbing_Agent/1.0"}
        response = requests.post(OVERPASS_URL, data={'data': query}, headers=headers)
        response.raise_for_status()
        data = response.json()
        
        spots = []
        for el in data.get("elements", []):
            tags = el.get("tags", {})
            spot_lat = el.get("lat") or el.get("center", {}).get("lat")
            spot_lon = el.get("lon") or el.get("center", {}).get("lon")
            if not spot_lat or not spot_lon:
                continue
                
            is_indoor = tags.get("indoor") == "yes" or tags.get("climbing:sport") == "indoor" or tags.get("leisure") == "sports_centre"
            spots.append({
                "id": el.get("id"),
                "name": tags.get("name", "Unknown Spot"),
                "lat": spot_lat,
                "lon": spot_lon,
                "is_indoor": is_indoor,
            })
        return spots
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find climbing spots using Overpass API.")
    parser.add_argument("--lat", type=float, required=True)
    parser.add_argument("--lon", type=float, required=True)
    parser.add_argument("--radius", type=int, default=50000, help="Search radius in meters")
    args = parser.parse_args()
    
    result = find_climbing_spots(args.lat, args.lon, args.radius)
    print(json.dumps(result, ensure_ascii=False))
