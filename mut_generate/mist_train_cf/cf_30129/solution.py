"""
QUESTION:
Write a function `maxProfit` that takes a list of integers `prices` as input, where each integer represents a daily stock price. The function should return the maximum possible profit that can be obtained by buying and selling the stock at most once. If no profit can be made, return 0.
"""

def entance(prices):
    if not prices:
        return 0
    
    max_profit = 0
    min_price = prices[0]
    
    for price in prices:
        if price < min_price:
            min_price = price
        else:
            max_profit = max(max_profit, price - min_price)
    
    return max_profit