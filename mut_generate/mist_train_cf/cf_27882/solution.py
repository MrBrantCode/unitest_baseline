"""
QUESTION:
Write a function `max_profit` that calculates the maximum possible profit from a list of daily stock prices. The function should take a list of integers as input and return an integer representing the maximum profit. The function must find the maximum profit by comparing all possible buy and sell combinations. If no profit can be made (i.e., less than two prices are given), return 0.
"""

def max_profit(prices):
    if len(prices) < 2:
        return 0

    max_profit = 0
    min_price = prices[0]

    for price in prices:
        if price < min_price:
            min_price = price
        else:
            max_profit = max(max_profit, price - min_price)

    return max_profit