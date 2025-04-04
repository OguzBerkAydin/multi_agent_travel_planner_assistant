"""
Travel plan node.
Creates a comprehensive travel plan based on all collected information.
"""
from typing import Dict, Any
from langchain_core.messages import HumanMessage

from ..agents.travel_planner_agent import TravelPlannerAgent
from ..state.travel_state import TravelState

def travel_plan_node(state: TravelState) -> Dict[str, Any]:
    """
    Create a comprehensive travel plan based on all collected information.
    
    Args:
        state: Current workflow state with all travel information
        
    Returns:
        Updated state with final travel plan
    """
    # Create travel planner agent
    travel_planner_agent = TravelPlannerAgent.create()
    
    # Check if we have enough information to create a plan
    missing_info = []
    if not state.get("city"):
        missing_info.append("city")
    if not state.get("travel_date"):
        missing_info.append("travel date")
    if not state.get("weather_info") or not state["weather_info"].get("forecast"):
        missing_info.append("weather information")
    if not state.get("city_info") or not state["city_info"].get("attractions"):
        missing_info.append("city attractions")
    if not state.get("hotel_info") or not state["hotel_info"].get("results"):
        missing_info.append("hotel options")
    if not state.get("budget_info") or not state["budget_info"].get("budget_plan"):
        missing_info.append("budget information")
    
    # If missing critical information, return error
    if missing_info:
        error_message = (
            f"Unable to create a complete travel plan due to missing information: "
            f"{', '.join(missing_info)}."
        )
        return {
            "travel_plan": error_message,
            "messages": state["messages"] + [HumanMessage(content=error_message)]
        }
    
    # Create comprehensive prompt for travel planner
    planning_prompt = f"""
    Create a comprehensive travel plan for {state['city']} on {state['travel_date']} based on the following information:

    WEATHER INFORMATION:
    {state['weather_info']['forecast']}

    CITY ATTRACTIONS AND CULTURAL PLACES:
    {state['city_info']['attractions']}

    HOTEL OPTIONS:
    {state['hotel_info']['results']}

    BUDGET AND EXCHANGE RATE INFORMATION:
    {state['budget_info']['budget_plan']}

    Please include:
    1. Daily itinerary with activities considering the weather and must-visit places
    2. Recommended hotel from the options with justification
    3. Detailed packing list based on the weather forecast
    4. Write curreny differance then Budget considerations and money management tips
    5. Cultural insights and special recommendations for this destination
    6. Transportation tips including from the airport to the city and getting around
    7. Local cuisine recommendations
    """
    
    # Invoke the travel planner agent
    response = travel_planner_agent.invoke(
        {"messages": [HumanMessage(content=planning_prompt)]}
    )
    
    # Extract the travel plan
    travel_plan = response["messages"][-1].content
    
    # Add the plan to messages for response to user
    updated_messages = state["messages"] + [HumanMessage(content=travel_plan)]
    
    return {
        "travel_plan": travel_plan, 
        "messages": updated_messages
    }