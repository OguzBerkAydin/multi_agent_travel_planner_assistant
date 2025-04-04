"""
Hotel search node.
Searches for hotel options and information.
"""
from typing import Dict, Any
from langchain_core.messages import HumanMessage

from ..agents.hotel_agent import HotelAgent
from ..state.travel_state import TravelState

def hotel_search_node(state: TravelState) -> Dict[str, Any]:
    """
    Search for hotel options in the target city.
    
    Args:
        state: Current workflow state with city information
        
    Returns:
        Updated state with hotel information
    """
    # Create hotel search agent
    hotel_agent = HotelAgent.create()
    
    # Validate required information
    if not state.get("city"):
        return {
            "hotel_info": {
                "results": "Unable to search for hotels due to missing city name.",
                "query_city": "Unknown"
            }
        }
    
    # Determine hotel search parameters based on travel date if available
    date_context = ""
    if state.get("travel_date"):
        date_context = f" for {state['travel_date']}"
    
    # Create query for hotel search
    hotel_query = (
        f"Find me the top 3 hotels in {state['city']}{date_context} with their ratings, "
        f"price ranges, and key amenities. Include both luxury and mid-range options. "
        f"For each hotel, provide the name, star rating, approximate price per night, "
        f"location/neighborhood, and at least 3 notable amenities or features."
    )
    
    # Invoke the hotel search agent
    response = hotel_agent.invoke(
        {"messages": [HumanMessage(content=hotel_query)]}
    )
    
    # Extract the response
    hotel_info = {
        "results": response["messages"][-1].content,
        "query_city": state["city"],
        "query_date": state.get("travel_date", "Unspecified")
    }
    
    return {"hotel_info": hotel_info}