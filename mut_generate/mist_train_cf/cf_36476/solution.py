"""
QUESTION:
Write a function `max_profit(prices)` that calculates the maximum profit that can be obtained by buying and selling a stock at most once from a given list of daily stock prices. The function should take a list of integers `prices` as input, where `prices[i]` is the price of the stock on the `i-th` day, and return the maximum possible profit. If no profit can be made, return 0.

The input list `prices` has the following constraints: 1 <= len(prices) <= 10^5 and 0 <= prices[i] <= 10^4.
"""

from typing import List

def entrance(prices: List[int]) -> int:
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