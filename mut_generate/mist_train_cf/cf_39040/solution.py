"""
QUESTION:
Write a function `max_profit(stock_prices)` that calculates the maximum profit from a list of daily stock prices, assuming only one transaction (buy and sell) is allowed and the buy must occur before the sell. If no profit can be made, return 0. The function should take a list of integers as input and return an integer.
"""

def max_profit(stock_prices):
    if not stock_prices:
        return 0
    
    min_price = stock_prices[0]
    max_profit = 0
    
    for price in stock_prices:
        if price < min_price:
            min_price = price
        else:
            max_profit = max(max_profit, price - min_price)
    
    return max_profit