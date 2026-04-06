from services.weather_service import get_weather

def weather_agent(destination):
    return get_weather(destination)