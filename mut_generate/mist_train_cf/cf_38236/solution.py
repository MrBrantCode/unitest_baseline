"""
QUESTION:
Write a function `max_profit(prices: List[int]) -> int` that takes a list of integers `prices` representing daily stock prices, where `prices[i]` is the price on the `i-th` day. The function should return the maximum possible profit from buying and selling the stock at most once. If no profit can be made, return 0. The input list `prices` has a length between 0 and 10^5 (inclusive), and each price is between 0 and 10^4 (inclusive).
"""

from typing import List

def maxProfit(prices: List[int]) -> int:
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