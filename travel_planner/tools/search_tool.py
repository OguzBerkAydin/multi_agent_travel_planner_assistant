"""
Search tool wrapper using Tavily Search API.
Provides search capabilities for finding hotels and other information.
"""
from langchain_community.tools.tavily_search import TavilySearchResults
from ..config.settings import get_tavily_api_key

def create_tavily_search_tool(max_results: int = 2) -> TavilySearchResults:
    """
    Create a Tavily search tool with specified parameters.
    
    Args:
        max_results: Maximum number of search results to return
        
    Returns:
        Configured TavilySearchResults tool
    """
    # Get API key from settings
    api_key = get_tavily_api_key()
    
    # Create and return the search tool
    return TavilySearchResults(
        max_results=max_results,
        api_key=api_key
    )