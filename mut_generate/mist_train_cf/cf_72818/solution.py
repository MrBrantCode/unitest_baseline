"""
QUESTION:
Write a function named `min_coins` that takes two parameters: a list of coin denominations and a target total value. Return the minimum number of coins required to reach the target value using the given coin denominations.
"""

def min_coins(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1