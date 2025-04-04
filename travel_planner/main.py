"""
Travel Planner Assistant Application.
Helps users plan trips by automatically gathering information.
"""
import argparse
from IPython.display import Image, display

from travel_planner.config.settings import initialize_environment
from travel_planner.state.travel_state import create_initial_state
from travel_planner.workflow.graph_builder import build_travel_planning_workflow, visualize_workflow

def parse_arguments():
    """
    Parse command line arguments.
    
    Returns:
        Parsed arguments
    """
    parser = argparse.ArgumentParser(description="Travel Planner Assistant")
    parser.add_argument(
        "--query", 
        type=str, 
        default="I'm planning a trip to Paris this saturday. Can you help me plan my trip?",
        help="Travel planning query"
    )
    parser.add_argument(
        "--visualize", 
        action="store_true", 
        help="Visualize the workflow graph"
    )
    return parser.parse_args()

def main():
    """
    Main application entry point.
    """
    # Parse command line arguments
    args = parse_arguments()
    
    # Initialize environment (API keys)
    initialize_environment()
    
    # Build the travel planning workflow
    travel_app = build_travel_planning_workflow()
    
    # Visualize the workflow if requested
    if args.visualize:
        workflow_image = visualize_workflow(travel_app)
        if workflow_image:
            print("\n===== WORKFLOW VISUALIZATION =====\n")
            display(Image(workflow_image))
        else:
            print("\nWorkflow visualization not available. Try installing required dependencies.")
    
    # Initialize with the user query
    user_query = args.query
    print(f"\n===== PROCESSING QUERY =====\n{user_query}\n")
    
    # Set up the initial state
    initial_state = create_initial_state(user_query)
    
    # Execute the workflow
    print("\n===== GENERATING TRAVEL PLAN =====\n")
    result = travel_app.invoke(initial_state)
    
    # Print the final travel plan
    print("\n===== FINAL TRAVEL PLAN =====\n")
    print(result["travel_plan"])
    
    # # Print additional information if needed
    # print("\n===== ADDITIONAL INFORMATION =====\n")
    # print(result['hotel_info']['results'])
    # print(result['weather_info']['forecast'])
    # print(result['travel_date'])
    # print("\n===== CITY INFORMATION =====\n")
    # print(result["city_info"]["attractions"])
    # print("\n===== BUDGET INFORMATION =====\n")
    # print(result["budget_info"]["budget_plan"])

if __name__ == "__main__":
    main()