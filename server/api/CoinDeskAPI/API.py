import requests
from time import time
import os

COINDESK_API_HOURLY_LIMIT = 2000

class CoinDeskAPI():
    def __init__(self):
        self.api_key = os.environ.get("COIN_DESK_API_KEY")
        self.base_url = "https://min-api.cryptocompare.com/data/v2"
        self.headers = {"Content-type":"application/json; charset=UTF-8", 
                        "api_key":self.api_key}

    def get_hourly_data(self, 
                        pair={'currency': 'gbp', 'crypto_currency': 'btc'}, 
                        limit='2000',
                        unix_timestamp=int(time())) -> dict:
        
        response = requests.get(
            f"{self.base_url}/histohour",
            params={"fsym":pair['crypto_currency'],"tsym":pair['currency'],"limit":limit, "toTs":unix_timestamp},
            headers={"Content-type":"application/json; charset=UTF-8", "api_key":self.api_key}
        )
        
        json_response = response.json()
        return json_response
    
if __name__ == "__main__":
    coin_desk_api = CoinDeskAPI()
    print(coin_desk_api.get_hourly_data(limit=10))
