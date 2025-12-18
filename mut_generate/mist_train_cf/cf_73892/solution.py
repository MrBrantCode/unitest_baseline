"""
QUESTION:
Write a function named `maxProfit` that takes a list of integers `prices` as input, where `prices[i]` represents the cost of a stock on the `ith` day. The function should return the maximum possible profit that can be achieved by buying and selling the stock any number of times, with the restriction that a new transaction cannot start before the previous one is completed. The length of the input list `prices` is between 1 and 3 * 10^4, and each element in the list is between 0 and 10^4.
"""

def maxProfit(prices):
    max_profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            max_profit += prices[i] - prices[i-1]
    return max_profit