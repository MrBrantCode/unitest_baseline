"""
QUESTION:
Write a function `findMinCoins(coins, amount)` that uses dynamic programming to find the minimum number of coins from the given list `coins` that sum up to the given `amount`. The function should return the minimum number of coins if possible, or -1 if no combination of coins can sum up to the `amount`.
"""

def findMinCoins(coins, amount):
    MAX = float('inf')
    dp = [0] + [MAX] * amount

    for i in range(1, amount + 1):
        dp[i] = min([dp[i - c] + 1 if i - c >= 0 else MAX for c in coins])

    return dp[amount] if dp[amount] != MAX else -1