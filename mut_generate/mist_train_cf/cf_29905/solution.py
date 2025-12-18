"""
QUESTION:
Write a function `maxProfit(prices)` that takes a list of integers `prices` representing daily stock prices and returns the maximum profit that can be obtained by buying and selling the stock at most once. If no profit can be made, return 0. The length of the list is at least 2 and at most 10^5. Each integer represents the price of a given stock on that day.
"""

def maxProfit(prices):
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