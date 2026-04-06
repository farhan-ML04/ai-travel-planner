from services.flight_service import get_flights

def flight_agent(destination, budget):
    return get_flights(destination, budget)