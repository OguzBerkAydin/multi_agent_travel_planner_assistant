"""
Travel planner agent.
Specialized agent for creating comprehensive travel plans.
"""
from .base_agent import BaseAgent

class TravelPlannerAgent(BaseAgent):
    """
    Agent specialized in creating comprehensive travel plans.
    """
    
    @staticmethod
    def create():
        """
        Create a travel planner agent.
        
        Returns:
            Configured travel planner agent
        """
        # This agent doesn't need external tools, it processes existing information
        return BaseAgent.create_agent([])