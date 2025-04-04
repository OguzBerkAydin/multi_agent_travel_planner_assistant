
## System Architecture

The travel planner uses a workflow orchestrated by LangGraph, where each step is handled by a specialized agent powered by Llama 3.3, a large language model from Groq. Here's the workflow:

1. **City Extraction** → **Date Extraction** → **Weather Information** → **City Attractions** → **Hotel Search** → **Budget Info** → **Final Travel Plan**

![alt text](workflow.png)

## Key Components

### 1. State Management
The system maintains a `TravelState` that tracks:
- User messages
- Destination city
- Travel date
- Weather information
- Accommodation options
- Budget considerations
- Attractions and city information
- The final travel plan

### 2. Specialized Agents

Each agent handles a specific task:

- **City & Date Extraction Agents**: Parse the user's query to identify where and when they want to travel
- **Weather Agent**: Gets forecast data and suggests appropriate clothing
- **City Info Agent**: Collects information about attractions and historical places
- **Hotel Agent**: Searches for accommodations with ratings and amenities
- **Exchange Rate Agent**: Provides currency exchange information and budget advice
- **Travel Planner Agent**: Combines all information into a cohesive travel plan

### 3. External API Integration

The system connects to several external services:
- OpenWeather API for weather forecasts
- Wikipedia API for historical attractions
- Exchange Rate API for currency conversion
- Tavily Search API for hotel information

## How It Works: Example Walkthrough

When a user inputs: "I'm planning a trip to San Francisco this saturday. Can you help me plan my trip?"

1. **City Extraction**: The system identifies "San Francisco" as the destination
2. **Date Extraction**: It determines "this saturday" as the travel date and converts it to YYYY-MM-DD format
3. **Weather Information**: Gets the forecast for San Francisco on that date and suggests appropriate clothing
4. **City Information**: Collects information about top attractions in San Francisco
5. **Hotel Search**: Finds and rates accommodation options
6. **Budget Planning**: Gets exchange rates between Turkish Lira and USD, suggests budget breakdown
7. **Travel Plan Creation**: Combines all information into a comprehensive travel plan including:
   - Daily activities based on weather and attractions
   - Recommended hotel
   - Packing list
   - Budget considerations
   - Cultural insights

### Example Output 
```
===== FINAL TRAVEL PLAN =====

**Comprehensive Travel Plan for San Francisco**

**Weather Forecast:**
For April 6, 2025, San Francisco is expected to be mostly cloudy with a high temperature of 16.46°C and a low of 11.65°C. The wind speed will be moderate, ranging from 0.62 to 4.63 m/s. There is a high probability of rain throughout the day, with the highest chance of rain at 21:00.

**Packing List:**

* Waterproof or water-resistant clothing, such as a jacket or umbrella, to protect against the rain
* Layers of breathable clothing, such as t-shirts, sweaters, and light jackets, to adjust to the changing temperatures
* Comfortable shoes or boots with good grip, in case of wet or slippery surfaces
* Warm clothing, such as a scarf or hat, for the cooler morning and evening hours
* Power adapter and charger for electronic devices
* Camera and charger for capturing memories
* Reusable water bottle and coffee cup to reduce waste
* Snacks and energy bars for quick energy boosts
* Travel documents, such as passport, visa, and travel insurance

**Daily Activities:**

Day 1:

* 9:00 AM: Start the day with a visit to the iconic **Union Square**, where you can explore the shops, cafes, and street performers.
* 11:00 AM: Take a short walk to the **San Francisco City Hall**, a stunning example of Beaux-Arts architecture.
* 1:00 PM: Grab lunch at a nearby restaurant, such as **Fisherman's Wharf**, where you can try some fresh seafood.
* 2:30 PM: Visit the **San Francisco Maritime National Historical Park**, which showcases the city's rich maritime history.
* 5:00 PM: Take a ride on the famous **San Francisco cable car system**, which offers breathtaking views of the city.

Day 2:

* 9:00 AM: Visit the **Mission San Francisco de Asís (Mission Dolores)**, a historic mission that dates back to 1776.
* 11:00 AM: Explore the **Presidio of San Francisco**, a former military base turned national park.
* 1:00 PM: Have lunch at a nearby cafe, such as **The Presidio Social Club**.
* 2:30 PM: Visit the **California Palace of the Legion of Honor**, a museum that features an impressive collection of art and artifacts.
* 5:00 PM: Take a stroll along the **San Francisco Bay Area**, which offers stunning views of the Golden Gate Bridge and the city skyline.

Day 3:

* 9:00 AM: Visit the **Treasure Island**, a man-made island in the San Francisco Bay that offers stunning views of the city and the bay.
* 11:00 AM: Explore the **National Register of Historic Places listings in San Francisco**, which includes a range of historic buildings and landmarks.
* 1:00 PM: Grab lunch at a nearby restaurant, such as **The Slanted Door**.
* 2:30 PM: Visit the **Old San Francisco Mint**, a historic building that now serves as a museum.
* 5:00 PM: Take a walk through the **Chinatown** neighborhood, which offers a unique glimpse into the city's vibrant cultural scene.

**Recommended Hotel:**
Based on the options provided, I recommend the **The Marker Union Square San Francisco**. This hotel offers a welcoming ambiance, attentive staff, and a quality onsite restaurant. The price starts from $250 per night, which is a good value considering the hotel's amenities and location.

**Budget Considerations and Money Management Tips:**

* Exchange some Turkish Lira for US Dollars, but also use credit cards for larger purchases to avoid exchange rate fluctuations.
* Set a daily budget of $200-300 per person, which should cover accommodation, meals, transportation, and attractions.
* Use public transportation, such as buses and trains, to get around the city, which is affordable and convenient.
* Take advantage of free attractions and activities, such as visiting the **Golden Gate Park** or exploring the **Haight-Ashbury** neighborhood.
* Consider purchasing a **San Francisco CityPASS**, which can help you save money on attractions and experiences.

**Cultural Insights and Special Recommendations:**

* San Francisco is a vibrant and diverse city, with a rich cultural scene. Be sure to explore the different neighborhoods, such as **Chinatown**, **Fisherman's Wharf**, and **Haight-Ashbury**, to experience the unique character of each area.
* Try some of the city's famous cuisine, such as **sourdough bread**, **fresh seafood**, and **Chinese dim sum**.
* Visit some of the city's iconic landmarks, such as the **Golden Gate Bridge**, **Alcatraz Island**, and **Lombard Street**.
* Take a **guided tour** of the city to learn more about its history, culture, and landmarks.
* Be sure to respect the city's diverse communities and cultures, and to follow local customs and traditions.

Overall, San Francisco is a unique and fascinating city that offers something for everyone. With its rich history, vibrant culture, and stunning natural beauty, it's a destination that's sure to leave you with unforgettable memories. 
```

## Technical Implementation

This system demonstrates advanced techniques in AI orchestration:
- **LangGraph**: For workflow management and agent coordination
- **ReAct Pattern**: Allows agents to reason and take actions
- **Tool Use**: Enables the language model to interact with external APIs
- **State Management**: Maintains context throughout the planning process

