import requests

def get_weather(city):
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
    geo_res = requests.get(geo_url).json()

    if "results" not in geo_res:
        return "Weather not found"

    lat = geo_res["results"][0]["latitude"]
    lon = geo_res["results"][0]["longitude"]

    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    weather_res = requests.get(weather_url).json()

    current = weather_res.get("current_weather", {})

    return f"Temperature: {current.get('temperature')}°C, Wind: {current.get('windspeed')} km/h"