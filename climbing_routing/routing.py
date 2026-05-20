import argparse
import json
import requests
import sys

sys.stdout.reconfigure(encoding='utf-8')

OSRM_URL = "http://router.project-osrm.org/route/v1/driving/"

def get_route(coords_list):
    # coords_list format is "lat1,lon1 lat2,lon2 lat3,lon3"
    points = coords_list.strip().split()
    if len(points) < 2:
        return {"error": "At least 2 points are required."}
        
    osrm_coords = []
    gmaps_origin = ""
    gmaps_dest = ""
    gmaps_waypoints = []
    
    for i, p in enumerate(points):
        lat, lon = p.split(',')
        osrm_coords.append(f"{lon},{lat}") # OSRM needs lon,lat
        if i == 0:
            gmaps_origin = f"{lat},{lon}"
        elif i == len(points) - 1:
            gmaps_dest = f"{lat},{lon}"
        else:
            gmaps_waypoints.append(f"{lat},{lon}")
            
    coords_str = ";".join(osrm_coords)
    url = f"{OSRM_URL}{coords_str}?overview=false"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        if data.get("code") == "Ok" and len(data.get("routes", [])) > 0:
            route = data["routes"][0]
            distance_km = route["distance"] / 1000.0
            duration_min = route["duration"] / 60.0
            
            gmaps_link = f"https://www.google.com/maps/dir/?api=1&origin={gmaps_origin}&destination={gmaps_dest}&travelmode=driving"
            if gmaps_waypoints:
                gmaps_link += f"&waypoints={'|'.join(gmaps_waypoints)}"
            
            return {
                "distance_km": round(distance_km, 2),
                "duration_min": round(duration_min, 0),
                "maps_link": gmaps_link
            }
        else:
            return {"error": "Route not found"}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate multi-stop route.")
    parser.add_argument("--coords", type=str, required=True, help='Space separated lat,lon e.g. "48.8,2.3 45.7,4.8"')
    args = parser.parse_args()
    
    result = get_route(args.coords)
    print(json.dumps(result, ensure_ascii=False))
