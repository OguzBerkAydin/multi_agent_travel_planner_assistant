"""
Exchange rate agent.
Specialized agent for providing currency exchange rates and budget information.
"""
from .base_agent import BaseAgent
from ..tools.currency_tool import get_currency_rates

class ExchangeRateAgent(BaseAgent):
    """
    Agent specialized in currency exchange and budget information.
    """
    
    @staticmethod
    def create():
        """
        Create an exchange rate agent with appropriate tools.
        
        Returns:
            Configured exchange rate agent
        """
        return BaseAgent.create_agent([get_currency_rates])