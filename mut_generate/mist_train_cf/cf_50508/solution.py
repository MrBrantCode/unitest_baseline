"""
QUESTION:
Write a function `maxProfit(prices)` that calculates the maximum possible profit from buying and selling stocks given an array of stock prices `prices`, where `prices[i]` represents the stock price on the `i-th` day. You can make an infinite number of transactions, but you cannot engage in multiple transactions at the same time. The function should return the maximum possible profit. The input array `prices` will contain between 1 and 3*10^4 elements, and each element will be an integer between 0 and 10^4.
"""

def maxProfit(prices):
    max_profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            max_profit += prices[i] - prices[i-1]
    return max_profit