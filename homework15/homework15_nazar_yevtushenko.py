import requests  # pip install requests
import os
from dotenv import load_dotenv
import json

load_dotenv()

WEATHER_ENDPOINT = 'http://api.openweathermap.org/data/2.5/weather'
API_KEY = os.getenv("WEATHER-API-KEY")
city = input('please fill up your city ')

def weather_now(city) -> str:
    '''
    Show current temprature, pressure and description of weather in chosen city now
    :return: str
    '''
    weather_params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(url=WEATHER_ENDPOINT, params=weather_params)
    url = response.url
    if response.status_code == 200:
        weather = response.json()['main']
        temp = weather['temp']
        pressure = weather['pressure']
        weather_description = response.json()['weather'][0]['description']
        return f'{temp = }, {pressure = }, {weather_description = }'
    else:
        try:
            response.raise_for_status()
        except:
            return response.json()['message']

if __name__ == '__main__':
    print(weather_now(city))