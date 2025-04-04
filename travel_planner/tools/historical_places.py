"""
Historical places tool using Wikipedia API.
Finds historical and cultural attractions in a specified city.
"""
import requests
from typing import List, Dict, Any, Optional

from langchain_core.tools import tool

@tool
def get_historical_places(city_name: str, limit: int = 10, language: str = "en") -> List[Dict[str, str]]:
    """
    Fetches historical places in the specified city using the Wikipedia API.
    
    Args:
        city_name: Name of the city to search for historical places
        limit: Maximum number of results to return (default: 10)
        language: Wikipedia language code (default: "en" - English)
        
    Returns:
        List of historical places information
    """
    # Wikipedia API endpoint
    url = f"https://{language}.wikipedia.org/w/api.php"
    
    # Create search queries based on language
    search_queries = _generate_search_queries(city_name, language)
    
    all_results = []
    used_titles = set()  # Prevent duplicate titles
    
    # Process each search query
    for query in search_queries:
        try:
            results = _execute_wiki_search(url, query, limit, language)
            
            # Process and filter results
            for result in results:
                if result["title"] in used_titles:
                    continue
                    
                if _is_relevant_result(result, city_name):
                    place = {
                        "title": result["title"],
                        "snippet": _clean_snippet(result["snippet"])
                    }
                    all_results.append(place)
                    used_titles.add(result["title"])
                    
                    # Exit if we've reached the limit
                    if len(all_results) >= limit:
                        break
                        
            # Exit if we've reached the limit
            if len(all_results) >= limit:
                break
                
        except requests.exceptions.RequestException as e:
            continue
        except KeyError:
            continue
            
    return all_results

def _generate_search_queries(city_name: str, language: str) -> List[str]:
    """
    Generate appropriate search queries based on language.
    
    Args:
        city_name: City name to search for
        language: Wikipedia language code
        
    Returns:
        List of search queries
    """
    if language == "en":
        return [
            f"historical landmarks in {city_name}",
            f"historical monuments in {city_name}",
            f"museums in {city_name}",
            f"ancient sites in {city_name}"
        ]
    else:
        # Generic queries for other languages
        return [
            f"historical places {city_name}",
            f"{city_name} historical structures",
            f"{city_name} museums",
            f"{city_name} monuments"
        ]

def _execute_wiki_search(url: str, query: str, limit: int, language: str) -> List[Dict[str, Any]]:
    """
    Execute search against Wikipedia API.
    
    Args:
        url: Wikipedia API URL
        query: Search query
        limit: Maximum results to return
        language: Wikipedia language code
        
    Returns:
        List of search results
    """
    params = {
        "action": "query",
        "format": "json",
        "list": "search",
        "srsearch": query,
        "srlimit": limit,
        "srprop": "snippet"
    }
    
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    
    if "query" in data and "search" in data["query"]:
        return data["query"]["search"]
    return []

def _is_relevant_result(result: Dict[str, Any], city_name: str) -> bool:
    """
    Check if a search result is relevant to historical places in the city.
    
    Args:
        result: Search result dictionary
        city_name: City name to check against
        
    Returns:
        True if result is relevant
    """
    title = result["title"].lower()
    relevant_keywords = [
        "historical", "mosque", "palace", "museum", "monument", 
        "church", "cathedral", "temple", "castle", "ruins", "ancient"
    ]
    
    # Check if city name in title or any relevant keyword
    return (city_name.lower() in title or 
            any(keyword in title for keyword in relevant_keywords))

def _clean_snippet(snippet: str) -> str:
    """
    Clean HTML formatting from snippet text.
    
    Args:
        snippet: Raw snippet text with HTML
        
    Returns:
        Cleaned snippet text
    """
    return snippet.replace("<span class=\"searchmatch\">", "").replace("</span>", "")