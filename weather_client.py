import requests
from typing import Dict
import json

# connect to a "real" API

## Example: OpenWeatherMap
URL = "https://api.openweathermap.org/data/2.5/weather"

# TODO: get an API key from openweathermap.org and fill it in here!
API_KEY = "5ef2bbe1af34cdc5ad75db64c5cbd3d8"

def get_weather(city) -> Dict:
    res = requests.get(URL, params={"q": city, "appid": API_KEY})
    return res.json()

# TODO: try connecting to a another API! e.g. reddit (https://www.reddit.com/dev/api/)
# joke api

api_url = "https://official-joke-api.appspot.com/random_joke"

response_json = requests.get(api_url)
api_keys = response_json.json()
print(api_keys)

def main():
    temp = get_weather("London")
    print(temp)

if __name__ == "__main__":
    main()