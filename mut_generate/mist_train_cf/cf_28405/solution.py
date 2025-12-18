"""
QUESTION:
You are given a list of integers representing the prices of a stock on different days. Write a function `max_profit(prices: List[int]) -> int` to find the maximum profit that can be obtained by buying and selling the stock at most twice, with the restriction that you cannot engage in multiple transactions at the same time. The function should return the maximum possible profit.
"""

from typing import List

def maxProfit(prices: List[int]) -> int:
    n = len(prices)
    if n < 2:
        return 0

    max_profit1, max_profit2 = 0, 0
    min_price1, min_price2 = float('inf'), float('inf')

    for price in prices:
        min_price1 = min(min_price1, price)
        max_profit1 = max(max_profit1, price - min_price1)
        min_price2 = min(min_price2, price - max_profit1)
        max_profit2 = max(max_profit2, price - min_price2)

    return max_profit2