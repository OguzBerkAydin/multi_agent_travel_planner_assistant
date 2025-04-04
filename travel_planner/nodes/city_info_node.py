"""
City information node.
Retrieves historical places and attractions.
"""
from typing import Dict, Any
from langchain_core.messages import HumanMessage

from ..agents.city_info_agent import CityInfoAgent
from ..state.travel_state import TravelState

def city_info_node(state: TravelState) -> Dict[str, Any]:
    """
    Get information about historical places and attractions in the city.
    
    Args:
        state: Current workflow state with city information
        
    Returns:
        Updated state with city attractions information
    """
    # Create city information agent
    city_agent = CityInfoAgent.create()
    
    # Validate required information
    if not state.get("city"):
        return {
            "city_info": {
                "attractions": "Unable to retrieve city information due to missing city name.",
                "query_city": "Unknown"
            }
        }
    
    # Create query for city attractions
    city_query = (
        f"What are the most important cultural places and must-visit attractions in {state['city']}? "
        f"Please provide comprehensive information about places to visit, their historical "
        f"significance, and practical visitor information."
    )
    
    # Invoke the city information agent
    response = city_agent.invoke(
        {"messages": [HumanMessage(content=city_query)]}
    )
    
    # Extract the response
    city_info = {
        "attractions": response["messages"][-1].content,
        "query_city": state["city"]
    }
    
    return {"city_info": city_info}