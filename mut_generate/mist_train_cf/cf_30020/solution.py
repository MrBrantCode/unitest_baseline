"""
QUESTION:
Write a function `minCoinsNeeded(coins: List[int], amount: int) -> int` that takes in a list of distinct positive integers `coins` representing coin denominations and an integer `amount`, and returns the minimum number of coins needed to make up the `amount`. If the amount cannot be made up by any combination of the given coins, return -1. 

The input consists of two arguments: `coins` (1 <= len(coins) <= 100) and `amount` (1 <= amount <= 10^4). You may assume that you have an infinite number of each kind of coin and you may use each coin as many times as needed.
"""

from typing import List

def minCoinsNeeded(coins: List[int], amount: int) -> int:
    inf = float('inf')
    dp = [inf] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    return dp[amount] if dp[amount] != inf else -1