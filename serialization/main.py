import requests
from classes import temperature_converter, Weather

def main():
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
    api_key = "72256f3b701ba9ac41e89ebf6bb62a98"

    city = input('Enter City: ')

    url = BASE_URL + "appid=" + api_key + "&q=" + city 

    response = requests.get(url).json()

    temp_k = response['main']['temp']
    feels_like_k = response['main']['feels_like']

    temp_converter = temperature_converter(temp_k)
    feels_converter = temperature_converter(feels_like_k)

    temp_c, temp_f = temp_converter.kelvin_to_cels_fahr()

    weather_description = response['weather'][0]['description']
    humidity = response['main']['humidity']

    weather_data = Weather(None, None, None, None)
    weather_data.set_temperature(temp_c)
    weather_data.set_description(weather_description)
    weather_data.set_humidity(humidity)
    weather_data.set_feels_like(temp_c)

    # Print the weather details
    print("Temperature:", weather_data.get_temperature(), "°C")
    print("Temperature:", temp_f, "°F")
    print("Description:", weather_data.get_description())
    print("Humidity:", weather_data.get_humidity(),'%')
    print("Feels Like:", weather_data.get_feels_like(), "°C")

if __name__ == '__main__':
    main()
else:
    print("This is an imported file")