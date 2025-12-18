"""
QUESTION:
Write a function `maxProfit` that takes in a list of integers `prices` representing daily stock prices and returns the maximum profit from at most one buy and sell transaction, with the restriction that a stock cannot be sold before it is bought.
"""

from typing import List

def maxProfit(prices: List[int]) -> int:
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