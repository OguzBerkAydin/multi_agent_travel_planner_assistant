"""
Hotel search agent.
Specialized agent for finding hotel options and information.
"""
from .base_agent import BaseAgent
from ..tools.search_tool import create_tavily_search_tool

class HotelAgent(BaseAgent):
    """
    Agent specialized in searching for hotel information.
    """
    
    @staticmethod
    def create():
        """
        Create a hotel search agent with appropriate tools.
        
        Returns:
            Configured hotel search agent
        """
        tavily_tool = create_tavily_search_tool(max_results=3)
        return BaseAgent.create_agent([tavily_tool])