"""
QUESTION:
Write a function `coinChange(coins, amount)` that takes a list of coin denominations `coins` and a total `amount` of money as input, and returns the fewest number of coins needed to make up the given amount. If the amount cannot be made up by any combination of the coins, return -1.
"""

def coinChange(coins, amount):
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    if dp[amount] == float("inf"):
        return -1
    return dp[amount]