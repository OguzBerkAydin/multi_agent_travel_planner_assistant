"""
Weather information node.
Retrieves weather forecast and clothing recommendations.
"""
from typing import Dict, Any
from langchain_core.messages import HumanMessage

from ..agents.weather_agent import WeatherAgent
from ..state.travel_state import TravelState

def weather_node(state: TravelState) -> Dict[str, Any]:
    """
    Get weather forecast and clothing recommendations for the travel destination.
    
    Args:
        state: Current workflow state with city and date information
        
    Returns:
        Updated state with weather information
    """
    # Create weather agent
    weather_agent = WeatherAgent.create()
    
    # Validate required information
    if not state.get("city") or not state.get("travel_date"):
        return {
            "weather_info": {
                "forecast": "Unable to retrieve weather information due to missing city or date.",
                "query_city": state.get("city", "Unknown")
            }
        }
    
    # Create query for weather and clothing recommendations
    weather_query = (
        f"What's the weather in {state['city']} on {state['travel_date']}? "
        f"Also, what clothes should I pack for this weather?"
    )
    
    # Invoke the weather agent
    response = weather_agent.invoke(
        {"messages": [HumanMessage(content=weather_query)]}
    )
    
    # Extract the response
    weather_info = {
        "forecast": response["messages"][-1].content,
        "query_city": state["city"],
        "query_date": state["travel_date"]
    }
    
    return {"weather_info": weather_info}