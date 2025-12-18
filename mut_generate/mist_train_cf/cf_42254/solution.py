"""
QUESTION:
Create a function named `close_all_orders` that takes two parameters: `orders` and `market_bearish`. The `orders` parameter is a list of integers representing buy and sell orders, where negative values represent buy orders and positive values represent sell orders. The `market_bearish` parameter is a boolean indicating whether the market is bearish (True) or bullish (False). 

If the market is bearish, the function should return a list with all buy orders removed from the input list. If the market is bullish, the function should return a list with all sell orders removed from the input list.
"""

def close_all_orders(orders, market_bearish):
    if market_bearish:
        return [order for order in orders if order < 0]
    else:
        return [order for order in orders if order > 0]