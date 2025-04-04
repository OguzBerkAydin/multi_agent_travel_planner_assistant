"""
Workflow graph builder.
Creates and configures the travel planning workflow.
"""
from langgraph.graph import StateGraph, END

from ..state.travel_state import TravelState
from ..nodes.extract_city import extract_city_node
from ..nodes.extract_date import extract_date_node
from ..nodes.weather_node import weather_node
from ..nodes.city_info_node import city_info_node
from ..nodes.hotel_search_node import hotel_search_node
from ..nodes.exchange_rate_node import exchange_rate_node
from ..nodes.travel_plan_node import travel_plan_node

def build_travel_planning_workflow():
    """
    Build the travel planning workflow graph.
    
    Returns:
        Compiled workflow graph
    """
    # Initialize the graph with the TravelState type
    workflow = StateGraph(TravelState)
    
    # Add nodes to the graph
    workflow.add_node("extract_city", extract_city_node)
    workflow.add_node("extract_date", extract_date_node)
    workflow.add_node("get_weather", weather_node)
    workflow.add_node("get_city_info", city_info_node)
    workflow.add_node("search_hotels", hotel_search_node)
    workflow.add_node("get_budget_info", exchange_rate_node)
    workflow.add_node("create_travel_plan", travel_plan_node)
    
    # Define the sequential flow
    workflow.set_entry_point("extract_city")
    
    # Configure the workflow edges
    # City -> Date -> Weather -> City Info -> Hotel -> Budget -> Travel Plan -> END
    workflow.add_edge("extract_city", "extract_date")
    workflow.add_edge("extract_date", "get_weather")
    workflow.add_edge("get_weather", "get_city_info")
    workflow.add_edge("get_city_info", "search_hotels")
    workflow.add_edge("search_hotels", "get_budget_info")
    workflow.add_edge("get_budget_info", "create_travel_plan")
    workflow.add_edge("create_travel_plan", END)
    
    # Compile the graph
    return workflow.compile()

def visualize_workflow(workflow):
    """
    Generate a visualization of the workflow graph.
    
    Args:
        workflow: Compiled workflow
        
    Returns:
        Mermaid PNG image of the workflow graph
    """
    try:
        return workflow.get_graph().draw_mermaid_png()
    except Exception:
        # This requires some extra dependencies and is optional
        print("Unable to generate workflow visualization. Missing dependencies.")
        return None