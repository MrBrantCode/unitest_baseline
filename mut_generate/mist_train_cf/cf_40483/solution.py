"""
QUESTION:
Write a function `maxProfit` that takes in a list of integers `prices` representing the stock prices on different days in chronological order, where the list has at least two elements. Return the maximum profit that can be obtained by buying and selling the stock on different days, with at most one transaction (i.e., buy one and sell one share of the stock).
"""

def maxProfit(prices):
    if not prices or len(prices) == 1:
        return 0
    
    max_profit = 0
    min_price = prices[0]
    
    for price in prices:
        if price < min_price:
            min_price = price
        else:
            max_profit = max(max_profit, price - min_price)
    
    return max_profit