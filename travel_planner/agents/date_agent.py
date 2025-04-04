"""
Date extraction agent.
Specialized agent for extracting and formatting dates from user input.
"""
from .base_agent import BaseAgent

class DateAgent(BaseAgent):
    """
    Agent specialized in extracting and formatting dates.
    """
    
    @staticmethod
    def create():
        """
        Create a date extraction agent.
        
        Returns:
            Configured date agent
        """
        # This agent doesn't need external tools
        return BaseAgent.create_agent([])