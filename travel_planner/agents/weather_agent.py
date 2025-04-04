"""
Weather information agent.
Specialized agent for retrieving weather forecasts and clothing recommendations.
"""
from .base_agent import BaseAgent
from ..tools.weather_tool import get_weather

class WeatherAgent(BaseAgent):
    """
    Agent specialized in retrieving weather information and clothing recommendations.
    """
    
    @staticmethod
    def create():
        """
        Create a weather agent with appropriate tools.
        
        Returns:
            Configured weather agent
        """
        return BaseAgent.create_agent([get_weather])