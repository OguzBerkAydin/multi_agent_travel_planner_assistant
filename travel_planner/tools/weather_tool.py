"""
Weather forecast tool using OpenWeatherMap API.
Provides weather information for a specific city and date.
"""
import requests
from datetime import datetime
from typing import Dict, Any, Union, List

from langchain_core.tools import tool
from ..config.settings import get_openweather_api_key

@tool
def get_weather(city: str, date: str) -> Union[Dict[str, Any], str]:
    """
    Retrieves weather forecast for a specified city and date.
    
    Args:
        city: The name of the city for which weather information is requested
        date: The date in "YYYY-MM-DD" format
        
    Returns:
        Dict with weather information or error message string
    """
    url = "https://api.openweathermap.org/data/2.5/forecast"
    api_key = get_openweather_api_key()
    
    # API parameters
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric",
        "cnt": 40  # Retrieves data in 3-hour intervals for up to 5 days
    }
    
    try:
        # Make API request
        response = requests.get(url, params=params)
        data = response.json()
        
        if response.status_code == 200:
            # Filter forecasts for the requested date
            selected_date_weather = _extract_date_forecasts(data, date)
            
            if selected_date_weather:
                return {
                    'City': data['city']['name'],
                    'Date': date,
                    'Forecasts': selected_date_weather
                }
            else:
                return f"No weather data found for {date}."
                
        else:
            return f"Error: {data.get('message', 'Unknown error')}"
            
    except Exception as e:
        return f"An error occurred: {str(e)}"

def _extract_date_forecasts(data: Dict[str, Any], target_date: str) -> List[Dict[str, Any]]:
    """
    Extract forecasts for a specific date from weather data.
    
    Args:
        data: Weather API response data
        target_date: Date to filter forecasts for (YYYY-MM-DD)
        
    Returns:
        List of forecast data points for the target date
    """
    forecast_list = data['list']
    selected_date_weather = []
    
    for forecast in forecast_list:
        forecast_time = datetime.utcfromtimestamp(forecast['dt']).strftime('%Y-%m-%d')
        
        if forecast_time == target_date:
            selected_date_weather.append({
                'time': datetime.utcfromtimestamp(forecast['dt']).strftime('%H:%M'),
                'temperature': forecast['main']['temp'],
                'wind_speed': forecast['wind']['speed'],
                'rain_probability': forecast.get('clouds', {}).get('all', 0),
                'weather_main': forecast.get('weather', [{}])[0].get('main', ''),
                'weather_description': forecast.get('weather', [{}])[0].get('description', '')
            })
            
    return selected_date_weather