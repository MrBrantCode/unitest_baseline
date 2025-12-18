"""
QUESTION:
Write a function `max_profit` that takes a list of integers representing daily stock prices as input and returns the maximum possible profit that can be achieved by buying and selling the stock. The function should assume that a stock must be bought before it can be sold.
"""

def max_profit(stock_prices):
    min_price = stock_prices[0]
    max_profit = 0

    for price in stock_prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)

    return max_profit