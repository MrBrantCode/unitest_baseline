"""
QUESTION:
Write a function `max_profit(prices: List[int]) -> int` to calculate the maximum possible profit from a single buy and sell operation given a list of daily stock prices. If no profit can be made, return 0. The function should only consider buying and selling the stock once.
"""

from typing import List

def max_profit(prices: List[int]) -> int:
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