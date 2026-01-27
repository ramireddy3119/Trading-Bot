import argparse
import os
import logging
from dotenv import load_dotenv

from bot.client import BinanceFuturesClient
from bot.orders import place_market_order, place_limit_order
from bot.validators import validate_inputs
from bot.logging_config import setup_logging

load_dotenv()
setup_logging()

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")

    parser.add_argument("--symbol", required=True, help="Trading symbol (e.g. BTCUSDT)")
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"])
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT"])
    parser.add_argument("--quantity", required=True, type=float)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:
        validate_inputs(
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )

        client = BinanceFuturesClient(
            api_key=os.getenv("BINANCE_API_KEY"),
            api_secret=os.getenv("BINANCE_API_SECRET")
        )

        print("\nOrder Request Summary")
        print("---------------------")
        print(f"Symbol   : {args.symbol}")
        print(f"Side     : {args.side}")
        print(f"Type     : {args.type}")
        print(f"Quantity : {args.quantity}")
        print(f"Price    : {args.price}")

        if args.type == "MARKET":
            response = place_market_order(
                client, args.symbol, args.side, args.quantity
            )
        else:
            response = place_limit_order(
                client, args.symbol, args.side, args.quantity, args.price
            )

        print("\nOrder Response")
        print("--------------")
        print(f"Order ID      : {response.get('orderId')}")
        print(f"Status        : {response.get('status')}")
        print(f"Executed Qty  : {response.get('executedQty')}")
        print(f"Avg Price     : {response.get('avgPrice', 'N/A')}")
        print("\n Order placed successfully")

    except Exception as e:
        logging.exception("Order failed")
        print(f"\n Order failed: {e}")

if __name__ == "__main__":
    main()
