"""
QUESTION:
Write a function `max_profit(prices)` that takes a list of integers representing stock prices and returns the maximum profit that can be obtained by buying and selling the stock at most once. If no profit can be made, return 0. The function should iterate through the list only once.
"""

from typing import List

def entance(prices: List[int]) -> int:
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