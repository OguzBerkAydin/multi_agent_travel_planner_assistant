"""
Currency exchange rate tool using exchangerate-api.com.
Provides current exchange rates between currencies.
"""
import requests
from typing import Dict, Any, Union, List, Optional

from langchain_core.tools import tool
from ..config.settings import get_exchange_rate_api_key

@tool
def get_currency_rates(base_currency: str = 'TRY', target_currencies: Optional[Union[str, List[str]]] = None) -> Dict[str, Any]:
    """
    Fetches currency exchange rate information.
    
    Args:
        base_currency: The base currency code (e.g., 'USD', 'EUR', default 'TRY')
        target_currencies: The target currency code(s) to convert to
            Can be a single currency code string or a list of currency codes
            
    Returns:
        Dictionary containing exchange rate data
    """
    api_key = get_exchange_rate_api_key()
    
    try:
        # Build the URL with the API key and base currency
        url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency}"
        
        # Fetch data from the API
        response = requests.get(url)
        
        # Check if the response is successful
        response.raise_for_status()
        
        # Parse the JSON response
        data = response.json()
        
        # Check if the API returned a successful response
        if data.get('result') != 'success':
            error_message = data.get('error', 'Unknown error')
            raise Exception(f"API Error: {error_message}")
            
        # Filter rates if target currencies are specified
        rates = _filter_rates(data['conversion_rates'], target_currencies)
        
        # Return only the needed information
        return {
            'base': base_currency,
            'date': data['time_last_update_utc'],
            'rates': rates
        }
        
    except requests.exceptions.RequestException as e:
        return {
            'error': f"Error fetching currency rates: {str(e)}",
            'base': base_currency,
            'rates': {}
        }
    except Exception as e:
        return {
            'error': f"Unexpected error: {str(e)}",
            'base': base_currency,
            'rates': {}
        }

def _filter_rates(
    rates: Dict[str, float], 
    target_currencies: Optional[Union[str, List[str]]]
) -> Dict[str, float]:
    """
    Filter exchange rates to only include requested currencies.
    
    Args:
        rates: Dictionary of all exchange rates
        target_currencies: Target currency code(s) to filter for
        
    Returns:
        Filtered dictionary of exchange rates
    """
    # If no target currencies specified, return all rates
    if not target_currencies:
        return rates
        
    # Convert single currency to list format
    if isinstance(target_currencies, str):
        target_currencies = [target_currencies]
        
    # Filter rates to only include requested currencies
    filtered_rates = {
        currency: rates[currency] 
        for currency in target_currencies 
        if currency in rates
    }
    
    return filtered_rates