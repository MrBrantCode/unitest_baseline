"""
QUESTION:
Create a function `max_profit(prices)` where `prices` is a list of integers representing the stock prices at different times. The function should return the maximum profit that can be achieved by making a single buy and sell transaction, where the buy must occur before the sell.
"""

def max_profit(prices):
    if not prices:
        return 0

    min_price = prices[0]
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        else:
            max_profit = max(max_profit, price - min_price)

    return max_profit