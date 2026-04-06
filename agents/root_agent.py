from agents.flight_agent import flight_agent
from agents.hotel_agent import hotel_agent
from agents.weather_agent import weather_agent
from agents.attraction_agent import attraction_agent
from utils.llm import get_llm

def plan_trip(destination, budget):

    flights = flight_agent(destination, budget)
    hotels = hotel_agent(destination)
    weather = weather_agent(destination)
    attractions = attraction_agent(destination)

    model = get_llm()

    prompt = f"""
    Plan a 3-day trip to {destination}.

    Flights:
    {flights}

    Hotels:
    {hotels}

    Weather:
    {weather}

    Attractions:
    {attractions}

    Create a clean day-wise itinerary.
    """

    response = model.generate_content(prompt)

    return response.text