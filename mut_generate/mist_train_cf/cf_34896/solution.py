"""
QUESTION:
Write a function `maxProfit` that takes a list of integers representing daily stock prices as input and returns the maximum possible profit from a single buy and sell transaction. If no profit can be made, return 0. Assume the list contains at least one element and is not empty.
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