"""
QUESTION:
You are given a list of stock prices where each element represents the price of a given stock on a particular day. Write a function `max_profit_twice(prices)` that calculates the maximum profit that can be obtained by buying and selling a stock at most twice. The function should have a time complexity of O(n), where n is the length of the input list.
"""

from typing import List

def max_profit_twice(prices: List[float]) -> float:
    if not prices:
        return 0

    n = len(prices)
    max_profit = 0
    first_transaction = [0] * n
    second_transaction = [0] * n

    min_price = prices[0]
    for i in range(1, n):
        min_price = min(min_price, prices[i])
        first_transaction[i] = max(first_transaction[i-1], prices[i] - min_price)

    max_price = prices[n-1]
    for i in range(n-2, -1, -1):
        max_price = max(max_price, prices[i])
        second_transaction[i] = max(second_transaction[i+1], max_price - prices[i])

    for i in range(n):
        max_profit = max(max_profit, first_transaction[i] + second_transaction[i])

    return max_profit