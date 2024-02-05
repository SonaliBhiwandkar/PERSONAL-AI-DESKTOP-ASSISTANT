# stock_handler.py
import requests
import json

Stock_API_KEY = "API KEY"  # Replace with your actual Alpha Vantage API key

def get_stock_data(symbol):
    try:
        base_url = "API URL"
        params = {
            'function': 'GLOBAL_QUOTE',
            'symbol': symbol,
            'apikey': Stock_API_KEY
        }

        response = requests.get(base_url, params=params)
        data = response.json()

        if 'Global Quote' in data:
            stock_info = data['Global Quote']
            return stock_info
        else:
            print("Invalid symbol or data not available.")
            return None

    except Exception as e:
        print(f"Error fetching stock data: {e}")
        return None
