"""
QUESTION:
Write a function `coin_combinations(amount: int, coins: List[int]) -> int` that takes in two parameters: an integer `amount` and a list of distinct positive integers `coins`. The function should return the number of combinations that make up the `amount` using any number of coins of the available denominations. Assume that you have an infinite number of each kind of coin. The restrictions are 1 <= amount <= 5000 and 1 <= len(coins) <= 50.
"""

from typing import List

def coin_combinations(amount: int, coins: List[int]) -> int:
    dp = [0] * (amount + 1)
    dp[0] = 1

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]

    return dp[amount]