#Binance Futures Testnet Trading Bot (Python)

##Overview

This project is a simplified Python trading bot that places orders on Binance Futures Testnet (USDT-M) using a clean, reusable, and well-structured codebase.

The application supports:

Market and Limit orders

BUY and SELL sides

Command-line input

Proper validation, logging, and error handling

This project is intended as a technical assessment and does not implement any trading strategy.

Features (Mapped to Task Requirements)
Core Requirements

Language: Python 3.x

Exchange: Binance Futures Testnet (USDT-M)
Order Types:
MARKET
LIMIT
Order Sides:
BUY
SELL
CLI Interface using argparse
Structured Codebase:
Separate API client, order logic, validation, logging, and CLI layers
Logging:
API requests
API responses
Errors and exceptions
Exception Handling:
Invalid input
API errors
Network issues


#Setup Instructions

##Step 1: Clone the Repository
git clone https://github.com/ramireddy3119/Trading-Bot
cd trading_bot

##Step 2: Create and Activate Virtual Environment
###Windows (PowerShell):
python -m venv .venv
.venv\Scripts\Activate
###Linux / macOS:
python3 -m venv .venv
source .venv/bin/activate

##Step 3: Install Dependencies
pip install -r requirements.txt

##Step 4: Create Environment Variables
Create a file named .env in the project root:
BINANCE_API_KEY=your_testnet_api_key
BINANCE_API_SECRET=your_testnet_secret_key

##Step 5: Run the Application
###Place a MARKET Order
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002
###Place a LIMIT Order
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.002 --price 80000

##Step 6: Verify Logs
logs/trading_bot.log
