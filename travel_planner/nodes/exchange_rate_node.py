"""
Exchange rate node.
Provides currency exchange rates and budget information.
"""
from typing import Dict, Any
from langchain_core.messages import HumanMessage

from ..agents.exchange_rate_agent import ExchangeRateAgent
from ..state.travel_state import TravelState

def exchange_rate_node(state: TravelState) -> Dict[str, Any]:
    """
    Get currency exchange rates and budget information for the trip.
    
    Args:
        state: Current workflow state with city and hotel information
        
    Returns:
        Updated state with budget and exchange rate information
    """
    # Create exchange rate agent
    exchange_rate_agent = ExchangeRateAgent.create()
    
    # Validate required information
    if not state.get("city"):
        return {
            "budget_info": {
                "budget_plan": "Unable to provide budget information due to missing city name.",
                "query_city": "Unknown"
            }
        }
    
    # Extract hotel information if available
    hotel_context = ""
    if state.get("hotel_info") and state["hotel_info"].get("results"):
        hotel_context = f"based on these hotel options: {state['hotel_info']['results']}"
    
    # Create query for exchange rate and budget information
    exchange_query = f"""
    I'm planning a trip from Turkey to {state['city']}.

    1. First, determine the local currency used in {state['city']}.
    2. Get the current exchange rate between Turkish Lira (TRY) and the local currency of {state['city']}.
    3. Based on this exchange rate, provide me with a budget breakdown for my trip to {state['city']} {hotel_context}.

    Consider these typical expenses categories:
    - Accommodation (based on the hotels you found)
    - Meals (budget, mid-range, and high-end options)
    - Local transportation
    - Attractions and activities
    - Shopping

    Also suggest how much money I should exchange or if I should use credit cards.
    Compare costs between Turkey and {state['city']} to help me understand the relative expenses.
    """
    
    # Invoke the exchange rate agent
    response = exchange_rate_agent.invoke(
        {"messages": [HumanMessage(content=exchange_query)]}
    )
    
    # Extract the response
    budget_info = {
        "budget_plan": response["messages"][-1].content,
        "query_city": state["city"]
    }
    
    return {"budget_info": budget_info}