"""
QUESTION:
Write a function `minCoins(amount: int, coins: List[int]) -> int` that returns the minimum number of coins required to make the given amount using any number of coins of each denomination in the list `coins`, which is sorted in ascending order and contains distinct positive integers. The given `amount` is a positive integer.
"""

from typing import List

def minCoins(amount: int, coins: List[int]) -> int:
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for currAmount in range(1, amount + 1):
        for coin in coins:
            if coin <= currAmount:
                dp[currAmount] = min(dp[currAmount], 1 + dp[currAmount - coin])
            else:
                break
    
    return dp[amount] if dp[amount] != float('inf') else -1