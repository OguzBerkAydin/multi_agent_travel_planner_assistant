# Travel Planner Assistant

An AI-powered travel planning system that automatically creates comprehensive travel plans based on natural language requests. The system gathers information about destinations, including weather forecasts, hotel options, local attractions, and budget recommendations.

## Features

- **City and Date Extraction**: Identifies travel destination and dates from natural language
- **Weather Information**: Provides weather forecasts and packing recommendations
- **Local Attractions**: Gathers information about historical places and attractions
- **Hotel Options**: Finds accommodation options with ratings and amenities
- **Budget Planning**: Provides currency exchange rates and expense breakdowns
- **Comprehensive Planning**: Creates detailed travel itineraries with practical advice

## System Architecture

The Travel Planner uses a workflow of specialized agents built with LangChain, LangGraph, and Groq LLM:

1. **Extract City** → **Extract Date** → **Get Weather** → **Get City Info** → **Search Hotels** → **Get Budget Info** → **Create Travel Plan**

Each step is handled by a specialized agent that focuses on a specific aspect of travel planning.

## Requirements

- Python 3.8+
- Required API keys:
  - Groq API Key (for LLM)
  - Tavily API Key (for search)
  - OpenWeather API Key (for weather)
  - Exchange Rate API Key (for currency)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/travel-planner.git
   cd travel-planner
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up environment variables for the required API keys:
   ```
   export GROQ_API_KEY="your-groq-api-key"
   export TAVILY_API_KEY="your-tavily-api-key"
   export OPENWEATHER_API_KEY="your-openweather-api-key"
   export EXCHANGE_RATE_API_KEY="your-exchange-rate-api-key"
   ```

## Usage

### Command Line Interface

Run the Travel Planner with a query:

```
python main.py --query "I'm planning a trip to Paris next weekend. Can you help me plan my trip?"
```

Visualize the workflow (requires extra dependencies):

```
python main.py --query "I'm planning a trip to Paris next weekend." --visualize
```

### Google Colab

You can also run the Travel Planner in Google Colab:

1. Open the `travel_planner_colab.ipynb` notebook in Google Colab
2. Follow the setup instructions to upload the code and set API keys
3. Run the cells to generate travel plans

### Example Queries

- "I'm planning a trip to Tokyo next month. Can you help me plan my trip?"
- "I want to visit Barcelona for a weekend in June. Need travel advice."
- "Planning a family trip to London during Christmas break. Any suggestions?"

## Project Structure

```
travel_planner/
│
├── config/                 # Configuration and API key management
│   ├── __init__.py
│   └── settings.py
│
├── tools/                  # External API integrations
│   ├── __init__.py
│   ├── weather_tool.py     # OpenWeather API
│   ├── historical_places.py # Wikipedia API
│   ├── currency_tool.py    # Exchange rate API
│   └── search_tool.py      # Tavily search
│
├── agents/                 # Specialized AI agents
│   ├── __init__.py
│   ├── base_agent.py
│   ├── weather_agent.py
│   ├── hotel_agent.py
│   ├── city_info_agent.py
│   ├── exchange_rate_agent.py
│   ├── date_agent.py
│   └── travel_planner_agent.py
│
├── nodes/                  # Workflow execution steps
│   ├── __init__.py
│   ├── extract_city.py
│   ├── extract_date.py
│   ├── weather_node.py
│   ├── city_info_node.py
│   ├── hotel_search_node.py
│   ├── exchange_rate_node.py
│   └── travel_plan_node.py
│
├── state/                  # State management
│   ├── __init__.py
│   └── travel_state.py
│
├── workflow/               # Workflow graph management
│   ├── __init__.py
│   └── graph_builder.py
│
├── utils/                  # Utility functions
│   ├── __init__.py
│   └── date_utils.py
│
├── main.py                 # Application entry point
├── travel_planner_colab.ipynb # Colab notebook
└── requirements.txt        # Project dependencies
```

## API Keys

You'll need to obtain API keys from the following services:

1. **Groq API Key**: https://console.groq.com/
2. **Tavily API Key**: https://tavily.com/
3. **OpenWeather API Key**: https://openweathermap.org/api
4. **Exchange Rate API Key**: https://www.exchangerate-api.com/

## Extending the System

### Adding New Tools

1. Create a new tool file in the `tools/` directory
2. Implement the tool using the `@tool` decorator
3. Create a specialized agent for the tool in `agents/`
4. Add a new node in the `nodes/` directory
5. Update the workflow graph in `workflow/graph_builder.py`

### Customizing the LLM

You can change the LLM model by modifying the settings in `config/settings.py`:

```python
# Available LLM models
AVAILABLE_MODELS = {
    "llama-3.3-70b-versatile": "llama-3.3-70b-versatile",
    "llama-3.1-8b": "llama-3.1-8b",
    # Add other models as needed
}

# Default model to use
DEFAULT_MODEL = "llama-3.3-70b-versatile"
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- This project uses [LangChain](https://python.langchain.com/) and [LangGraph](https://python.langchain.com/docs/langgraph)
- LLM capabilities provided by [Groq](https://console.groq.com/)
- Search functionality by [Tavily](https://tavily.com/)
- Weather data from [OpenWeatherMap](https://openweathermap.org/)
- Currency exchange rates from [ExchangeRate-API](https://www.exchangerate-api.com/)
