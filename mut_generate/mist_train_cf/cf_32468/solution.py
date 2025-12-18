"""
QUESTION:
Write a function `maxProfit` that takes a list of integers `prices` representing daily stock prices and returns the maximum possible profit from buying and selling the stock at most once. If no profit can be made, return 0. Assume that buying and selling on the same day is not allowed and there are no transaction fees.
"""

def entance(prices):
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