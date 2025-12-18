"""
QUESTION:
Write a function `maxProfit(prices)` that takes a list of integers `prices` representing daily stock prices and returns the maximum possible profit from buying and selling the stock at most once. The length of the list is between 2 and 10^5, and each integer represents the price of a given stock on that day. If no profit can be made, return 0.
"""

def maxProfit(prices):
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