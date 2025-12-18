"""
QUESTION:
Implement a function called `coinChange` that calculates the minimum number of coins needed to reach a given `amount` using a list of available `coins`. The function should take two parameters: `amount` (the target amount) and `coins` (a list of coin denominations). Assume there is an infinite supply of coins for each denomination. The function should return the minimum number of coins needed.
"""

def coinChange(amount, coins):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], 1 + dp[i - coin])
    return dp[amount]