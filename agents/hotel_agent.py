from services.places_service import get_places

def hotel_agent(destination):
    return get_places(destination, "hotels")