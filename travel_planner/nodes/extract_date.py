"""
Date extraction node.
Extracts and formats travel date from user input.
"""
from typing import Dict, Any
from datetime import datetime
from langchain_core.messages import HumanMessage
from langchain_core.prompts import PromptTemplate

from ..agents.base_agent import BaseAgent
from ..state.travel_state import TravelState

def extract_date_node(state: TravelState) -> Dict[str, Any]:
    """
    Extract and format the travel date mentioned in the user's message.
    
    Args:
        state: Current workflow state
        
    Returns:
        Updated state with extracted travel date
    """
    # Get today's date for context
    todays_date = datetime.today().strftime("%Y-%m-%d")
    
    # Extract the latest user message
    user_message = state["messages"][-1].content
    
    # Create a prompt for date extraction
    prompt = PromptTemplate(
        input_variables=["text", "todays_date"],
        template="""You are a date parsing assistant. Convert natural language date expressions to YYYY-MM-DD format. 
        If the user mentions a day of the week, assume it's for the upcoming week. 
        Return only the date with no additional text. 
        Today's date is: {todays_date}
        
        Request: {text}
        
        Date:"""
    )
    
    # Format the prompt with the user message and today's date
    message = HumanMessage(content=prompt.format(
        text=user_message, 
        todays_date=todays_date
    ))
    
    # Create LLM instance for extraction
    llm = BaseAgent.create_llm()
    
    # Invoke the LLM to extract the date
    travel_date = llm.invoke([message]).content.strip()
    
    return {"travel_date": travel_date}