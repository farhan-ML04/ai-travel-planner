import requests
import os

def get_places(city, category):
    api_key = os.getenv("GEOAPIFY_API_KEY")

    category_map = {
        "hotels": "accommodation.hotel",
        "tourist": "tourism.sights"
    }

    cat = category_map.get(category, "tourism.sights")

    # Get coordinates
    geo_url = f"https://api.geoapify.com/v1/geocode/search?text={city}&apiKey={api_key}"
    geo_res = requests.get(geo_url).json()

    if not geo_res.get("features"):
        return "Location not found"

    coords = geo_res["features"][0]["geometry"]["coordinates"]
    lon, lat = coords

    # Get places
    url = f"https://api.geoapify.com/v2/places?categories={cat}&filter=circle:{lon},{lat},5000&limit=5&apiKey={api_key}"
    res = requests.get(url).json()

    places = []
    for p in res.get("features", []):
        name = p["properties"].get("name", "Unknown")
        address = p["properties"].get("formatted", "")
        places.append(f"{name} - {address}")

    return "\n".join(places) if places else "No data"