"""
QUESTION:
Write a function `maxProfit` that takes a list of integers representing daily stock prices as input and returns the maximum profit that can be obtained by making a single transaction (buying one and selling one share of the stock). The function must sell the stock before buying again. The function should return 0 if the input list is empty.
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