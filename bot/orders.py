from binance.enums import SIDE_BUY, SIDE_SELL, ORDER_TYPE_MARKET, ORDER_TYPE_LIMIT, TIME_IN_FORCE_GTC

def place_market_order(client, symbol, side, quantity):
    return client.place_order(
        symbol=symbol,
        side=SIDE_BUY if side == "BUY" else SIDE_SELL,
        type=ORDER_TYPE_MARKET,
        quantity=quantity,
        recvWindow=5000
    )

def place_limit_order(client, symbol, side, quantity, price):
    return client.place_order(
        symbol=symbol,
        side=SIDE_BUY if side == "BUY" else SIDE_SELL,
        type=ORDER_TYPE_LIMIT,
        quantity=quantity,
        price=price,
        timeInForce=TIME_IN_FORCE_GTC,
        recvWindow=5000
    )
