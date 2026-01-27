import logging
from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceRequestException

class BinanceFuturesClient:
    def __init__(self, api_key: str, api_secret: str):
        self.client = Client(api_key, api_secret)
        self.client.FUTURES_URL = "https://testnet.binancefuture.com"

    def place_order(self, **kwargs):
        try:
            logging.info(f"Sending order request: {kwargs}")
            response = self.client.futures_create_order(**kwargs)
            logging.info(f"Order response: {response}")
            return response
        except BinanceAPIException as e:
            logging.error(f"Binance API error: {e}")
            raise
        except BinanceRequestException as e:
            logging.error(f"Network error: {e}")
            raise
