"""
Base agent functionality for creating specialized agents.
Provides common agent creation and configuration.
"""
from typing import List, Any

from langchain_groq import ChatGroq
from langgraph.prebuilt import create_react_agent
from langchain_core.tools import BaseTool

from ..config.settings import DEFAULT_MODEL, DEFAULT_TEMPERATURE

class BaseAgent:
    """
    Base class for creating specialized agents.
    """
    
    @staticmethod
    def create_llm(model_name: str = DEFAULT_MODEL, temperature: float = DEFAULT_TEMPERATURE) -> ChatGroq:
        """
        Create a language model instance.
        
        Args:
            model_name: Name of the Groq model to use
            temperature: Temperature setting for the LLM
            
        Returns:
            Configured ChatGroq instance
        """
        return ChatGroq(
            temperature=temperature,
            model_name=model_name
        )
    
    @staticmethod
    def create_agent(tools: List[BaseTool], model_name: str = DEFAULT_MODEL, temperature: float = DEFAULT_TEMPERATURE):
        """
        Create a ReAct agent with specified tools and model.
        
        Args:
            tools: List of tools available to the agent
            model_name: Name of the model to use
            temperature: Temperature setting for the LLM
            
        Returns:
            Configured ReAct agent
        """
        llm = BaseAgent.create_llm(model_name, temperature)
        return create_react_agent(llm, tools)