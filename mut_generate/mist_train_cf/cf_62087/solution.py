"""
QUESTION:
Design a function `maxProfit(prices)` that takes an array of stock prices as input and returns the maximum profit from trading the stock. The function should assume that a stock can only be held for at most one day and that buying and selling on the same day is not allowed. The function should run in O(n) time and use O(1) space.
"""

def maxProfit(prices):
    if len(prices) < 2:
        return 0

    buy = prices[0]
    max_profit = 0

    for price in prices[1:]:
        current_profit = price - buy
        max_profit = max(max_profit, current_profit)
        buy = min(buy, price)

    return max_profit