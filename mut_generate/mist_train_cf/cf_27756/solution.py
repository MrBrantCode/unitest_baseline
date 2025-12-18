"""
QUESTION:
Write a function `max_profit(stock_prices, days)` that calculates the maximum profit that can be obtained by buying and selling the stock within a certain number of days. The function should take two parameters: a list of integers `stock_prices` representing the daily stock prices of a certain company and an integer `days` representing the number of days for which the stock can be held before selling. The function should return the maximum possible profit.
"""

from typing import List

def entance(stock_prices: List[int], days: int) -> int:
    if not stock_prices or days <= 0:
        return 0

    n = len(stock_prices)
    if days >= n:
        return sum(max(0, stock_prices[i+1] - stock_prices[i]) for i in range(n-1))

    dp = [[0] * (days + 1) for _ in range(n)]
    for k in range(1, days + 1):
        max_diff = -stock_prices[0]
        for i in range(1, n):
            dp[i][k] = max(dp[i-1][k], stock_prices[i] + max_diff)
            max_diff = max(max_diff, dp[i][k-1] - stock_prices[i])
    return dp[n-1][days]