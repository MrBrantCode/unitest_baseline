"""
QUESTION:
Write a function `maxProfit(prices)` that takes a list of integers representing daily stock prices and returns the maximum possible profit from a single buy and sell transaction. If no profit can be made, return 0. Assume that buying and selling on the same day is not allowed, and use the maximum integer value 2147483647 as the initial minimum price to prevent overflow issues.
"""

from typing import List

def maxProfit(prices: List[int]) -> int:
    max_profit = 0
    min_price = 2147483647  
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
    return max_profit