#!/usr/bin/env python3
import argparse
import json
import requests
import sys
import hashlib

sys.stdout.reconfigure(encoding='utf-8')

OVERPASS_URL = "http://overpass-api.de/api/interpreter"

def get_simulated_price(hotel_id: int, tags: dict) -> int:
    """
    Simulate a realistic price based on the hotel's stars or its ID hash
    if stars are not available.
    """
    stars = tags.get("stars")
    if stars and stars.isdigit():
        return int(stars) * 30 + 20 # 2 stars = 80€, 3 stars = 110€, 4 stars = 140€
    
    # Hash the ID to get a consistent deterministic price between 50 and 150
    hash_val = int(hashlib.md5(str(hotel_id).encode()).hexdigest()[:8], 16)
    return 50 + (hash_val % 100)

def find_hotels(lat: float, lon: float, radius: int):
    query = f"""
    [out:json][timeout:25];
    (
      node["tourism"="hotel"](around:{radius},{lat},{lon});
      way["tourism"="hotel"](around:{radius},{lat},{lon});
      node["tourism"="hostel"](around:{radius},{lat},{lon});
      way["tourism"="hostel"](around:{radius},{lat},{lon});
    );
    out center;
    """
    try:
        headers = {"User-Agent": "Skile_IA_Climbing_Agent/1.0"}
        response = requests.post(OVERPASS_URL, data={'data': query}, headers=headers)
        response.raise_for_status()
        data = response.json()
        
        hotels = []
        for el in data.get("elements", []):
            tags = el.get("tags", {})
            spot_lat = el.get("lat") or el.get("center", {}).get("lat")
            spot_lon = el.get("lon") or el.get("center", {}).get("lon")
            if not spot_lat or not spot_lon:
                continue
                
            hotel_id = el.get("id")
            name = tags.get("name", "Unknown Hotel/Hostel")
            
            hotels.append({
                "id": hotel_id,
                "name": name,
                "lat": spot_lat,
                "lon": spot_lon,
                "website": tags.get("website", "N/A"),
                "estimated_price_eur": get_simulated_price(hotel_id, tags)
            })
        return hotels
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find hotels and accommodations using Overpass API.")
    parser.add_argument("--lat", type=float, required=True)
    parser.add_argument("--lon", type=float, required=True)
    parser.add_argument("--radius", type=int, default=10000, help="Search radius in meters")
    args = parser.parse_args()
    
    result = find_hotels(args.lat, args.lon, args.radius)
    print(json.dumps(result, ensure_ascii=False))
