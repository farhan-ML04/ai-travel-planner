from services.places_service import get_places

def attraction_agent(destination):
    return get_places(destination, "tourist")