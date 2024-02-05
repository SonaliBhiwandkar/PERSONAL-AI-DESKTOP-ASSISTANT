# weather_handler.py

import json
import urllib.request
import sys

def get_weather_data():
    try: 
        result_bytes = urllib.request.urlopen("API URL")
        return json.load(result_bytes)
    except urllib.error.HTTPError as e:
        handle_error(e)
    except urllib.error.URLError as e:
        handle_error(e)

def get_temperature(weather_data):
    return weather_data['currentConditions']['temp']

def get_conditions(weather_data):
    return weather_data['currentConditions']['conditions']

def get_description(weather_data):
    try:
        return weather_data['currentConditions'].get('description', 'Description not available')
    except KeyError:
        return "Description not available"

def handle_error(error):
    error_info = error.read().decode()
    print('Error code: ', error.code, error_info)
    sys.exit()
