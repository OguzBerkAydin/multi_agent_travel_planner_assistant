"""
State management for the Travel Planner application.
Defines the structure of the state that flows through the workflow.
"""
from typing import TypedDict, List, Dict, Any

class TravelState(TypedDict):
    """
    State structure to maintain data flow between agents.
    
    Attributes:
        messages: Store conversation messages
        city: Target city for travel
        travel_date: Travel date in YYYY-MM-DD format
        weather_info: Weather data and clothing recommendations
        hotel_info: Hotel search results
        city_info: City attractions and historical places
        budget_info: Currency exchange and budget breakdown
        travel_plan: Final compiled travel plan
    """
    messages: List[Any]            # Store conversation messages
    city: str                      # Target city for travel
    travel_date: str               # Travel date in YYYY-MM-DD format
    weather_info: Dict[str, Any]   # Weather data and clothing recommendations
    hotel_info: Dict[str, Any]     # Hotel search results
    city_info: Dict[str, Any]      # City attractions and historical places
    budget_info: Dict[str, Any]    # Currency exchange and budget breakdown
    travel_plan: str               # Final travel plan

def create_initial_state(user_query: str) -> TravelState:
    """
    Create an initial state with a user query.
    
    Args:
        user_query: Initial user query to start the workflow
        
    Returns:
        TravelState with initialized empty values
    """
    from langchain_core.messages import HumanMessage
    
    return {
        "messages": [HumanMessage(content=user_query)],
        "city": "",
        "travel_date": "",
        "weather_info": {},
        "city_info": {},
        "hotel_info": {},
        "budget_info": {},
        "travel_plan": ""
    }