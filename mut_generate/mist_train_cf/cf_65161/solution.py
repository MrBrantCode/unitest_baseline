"""
QUESTION:
Implement a function `maxProfit` that calculates the maximum possible profit from a given list of stock prices. The function should take a list of integers representing the daily stock prices as input and return an integer representing the maximum possible profit. The function should return 0 if the input list has less than 2 elements, as at least two prices are required to calculate a profit.
"""

def maxProfit(prices):
    if len(prices) < 2:
        return 0

    min_price = prices[0]
    max_profit = 0

    for i in range(1, len(prices)):
        # Update min price if found new min value
        if prices[i] < min_price:
            min_price = prices[i]
        # Update max profit if found new max profit
        elif prices[i] - min_price > max_profit:
            max_profit = prices[i] - min_price

    return max_profit