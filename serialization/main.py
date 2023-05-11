import asyncio
import os

import python_weather
from classes import Weather

async def get_weather_data(city: str) -> Weather:
    website = "https://www.weatherapi.com/"  # Replace with the actual website URL
    api_key = "0e5daea3e0f14ffdb2f222213231005"  # Replace with your API key
    
    client = python_weather.Client(format=python_weather.METRIC)
    await client.fetch(f"{website}/api?key={api_key}&q={city}")
    
    weather = client.api_response
    client.close()
        
    # Extract relevant weather information
    temperature = weather.current.temperature
    description = weather.current.sky_text
        
    return Weather(temperature, description)

def main():
    city = input("Enter a city: ")
    weather = asyncio.run(get_weather_data(city))
    
    # Print the weather details
    print(f"Temperature: {weather.get_temperature()}°C")
    print(f"Description: {weather.get_description()}")
    
if __name__ == '__main__':
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
  
    main()
