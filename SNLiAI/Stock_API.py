# Stock_API.py
import requests

class AlphaVantageStockAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "API URL"

    def get_stock_data(self, symbol):
        try:
            params = {
                'function': 'GLOBAL_QUOTE',
                'symbol': symbol,
                'apikey': self.api_key
            }

            response = requests.get(self.base_url, params=params)
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
