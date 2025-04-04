"""
City extraction node.
Extracts city information from user input.
"""
from typing import Dict, Any
from langchain_core.messages import HumanMessage
from langchain_core.prompts import PromptTemplate

from ..agents.base_agent import BaseAgent
from ..state.travel_state import TravelState

def extract_city_node(state: TravelState) -> Dict[str, Any]:
    """
    Extract the city mentioned in the user's message.
    
    Args:
        state: Current workflow state
        
    Returns:
        Updated state with extracted city
    """
    # Extract the latest user message
    user_message = state["messages"][-1].content
    
    # Create a prompt to extract the city
    prompt = PromptTemplate(
        input_variables=["text"],
        template="Extract the name of the city mentioned in the following request. Return only the city name with no additional text.\n\nRequest: {text}\n\nCity:"
    )
    
    # Format the prompt with the user message
    message = HumanMessage(content=prompt.format(text=user_message))
    
    # Create LLM instance for extraction
    llm = BaseAgent.create_llm()
    
    # Invoke the LLM to extract the city
    city = llm.invoke([message]).content.strip()
    
    return {"city": city}