"""
City information agent.
Specialized agent for retrieving historical places and attractions.
"""
from .base_agent import BaseAgent
from ..tools.historical_places import get_historical_places

class CityInfoAgent(BaseAgent):
    """
    Agent specialized in retrieving city information and attractions.
    """
    
    @staticmethod
    def create():
        """
        Create a city information agent with appropriate tools.
        
        Returns:
            Configured city information agent
        """
        return BaseAgent.create_agent([get_historical_places])