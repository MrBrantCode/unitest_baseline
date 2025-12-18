"""
QUESTION:
Write a function `max_profit(stock_prices)` that takes an array of daily stock prices as input and returns the maximum possible profit that can be achieved by buying and selling a stock, given that a stock must be owned before it can be sold.
"""

def max_profit(stock_prices):
    max_profit = 0
    min_price = stock_prices[0]

    for price in stock_prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)

    return max_profit