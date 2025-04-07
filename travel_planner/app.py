from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import Optional

from travel_planner.config.settings import initialize_environment
from travel_planner.state.travel_state import create_initial_state
from travel_planner.workflow.graph_builder import build_travel_planning_workflow

app = FastAPI(title="Travel Planner Assistant")

# Initialize environment and workflow once
initialize_environment()
travel_app = build_travel_planning_workflow()

class TravelRequest(BaseModel):
    query: str

@app.post("/plan-trip")
def plan_trip(request: TravelRequest):
    """
    Plan a trip based on a natural language query.
    """
    user_query = request.query

    # Set up the initial state
    initial_state = create_initial_state(user_query)

    # Execute the workflow
    result = travel_app.invoke(initial_state)

    return {
        "travel_plan": result.get("travel_plan", "No plan generated."),
        "city_info": result.get("city_info", {}),
        "hotel_info": result.get("hotel_info", {}),
        "weather_info": result.get("weather_info", {}),
        "budget_info": result.get("budget_info", {}),
        "travel_date": result.get("travel_date", {})
    }
