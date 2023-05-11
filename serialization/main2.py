import daytime as dt
import requests


BASE_URL = "http://api.openweathermap.org/data/weather?"
api_key = "72256f3b701ba9ac41e89ebf6bb62a98"

CITY = 'London'

url = BASE_URL + "appid=" + api_key + "&q=" + CITY 

response = requests.get(url).json()


print(response)