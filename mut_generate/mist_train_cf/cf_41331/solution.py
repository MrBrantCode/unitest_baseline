"""
QUESTION:
Write a function `maxProfit` that calculates the maximum profit from a list of integers `prices` representing daily stock prices. The function should find the maximum possible profit from buying and selling the stock once, with the condition that buying must occur before selling. If no profit is possible, return 0.

The input list `prices` contains at least one element, and stock prices are represented as integers.
"""

from typing import List

def maxProfit(prices: List[int]) -> int:
    min_price = prices[0]
    max_profit = 0
    
    for price in prices:
        if price < min_price:
            min_price = price
        else:
            max_profit = max(max_profit, price - min_price)
    
    return max_profit