"""
Configuration settings for the Travel Planner application.
Manages API keys and application settings.
"""
import os
import getpass
from typing import List, Dict, Any

# Available LLM models
AVAILABLE_MODELS = {
    "llama-3.3-70b-versatile": "llama-3.3-70b-versatile",
    "llama-3.1-8b": "llama-3.1-8b",
    # Add other models as needed
}

# Default model to use
DEFAULT_MODEL = "llama-3.3-70b-versatile"

# Default temperature setting
DEFAULT_TEMPERATURE = 0

# Required API keys
REQUIRED_API_KEYS = [
    "GROQ_API_KEY",
    "TAVILY_API_KEY",
    "OPENWEATHER_API_KEY",
    "EXCHANGE_RATE_API_KEY"
]

def initialize_environment() -> None:
    """
    Initialize environment variables for API keys.
    Prompts for missing keys if they are not set.
    """
    for key in REQUIRED_API_KEYS:
        _set_env(key)

def _set_env(var: str) -> None:
    """
    Set environment variable if not already set.
    
    Args:
        var: Name of the environment variable
    """
    if not os.environ.get(var):
        os.environ[var] = getpass.getpass(f"{var}: ")

def get_openweather_api_key() -> str:
    """Get OpenWeather API key from environment."""
    return os.environ.get("OPENWEATHER_API_KEY", "")

def get_tavily_api_key() -> str:
    """Get Tavily API key from environment."""
    return os.environ.get("TAVILY_API_KEY", "")

def get_groq_api_key() -> str:
    """Get Groq API key from environment."""
    return os.environ.get("GROQ_API_KEY", "")

def get_exchange_rate_api_key() -> str:
    """Get Exchange Rate API key from environment."""
    return os.environ.get("EXCHANGE_RATE_API_KEY", "")