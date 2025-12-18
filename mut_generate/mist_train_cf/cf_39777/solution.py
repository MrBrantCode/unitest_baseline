"""
QUESTION:
Write a function `max_profit(prices: List[int]) -> int` that takes a list of integers representing daily stock prices and returns the maximum possible profit from buying and selling the stock at most once. The length of the input list is between 2 and 10^5, and each price is an integer in the range [-10^4, 10^4].
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