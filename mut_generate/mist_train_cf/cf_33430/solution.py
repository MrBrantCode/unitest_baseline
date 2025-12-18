"""
QUESTION:
Write a function `max_profit` that takes a list of integers `prices` representing the prices of a stock on consecutive days. The function should return a tuple containing the maximum profit that can be made by buying and selling the stock once, and a tuple representing the 1-indexed buying and selling dates. If there are multiple solutions with the same maximum profit, return the one with the earliest buying date. The list `prices` contains at least one and at most 10^5 positive integers, each not exceeding 10^4.
"""

from typing import List, Tuple

def max_profit(prices: List[int]) -> Tuple[int, Tuple[int, int]]:
    min_price = prices[0]
    max_profit = 0
    buy_date = 1
    sell_date = 1

    for i, price in enumerate(prices):
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
            buy_date = prices.index(min_price) + 1
            sell_date = i + 1

    return max_profit, (buy_date, sell_date)