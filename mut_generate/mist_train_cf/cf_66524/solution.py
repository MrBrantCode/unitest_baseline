"""
QUESTION:
The function should be named `minCoins` and take two inputs: `coins`, a list of coin denominations, and `amount`, the total monetary value to be achieved. The function should return the minimum number of coins required to make the given amount using the available coin denominations. If it's not possible to make the amount with the given coins, the function should return -1. The solution should be efficient and scalable, handling large inputs and avoiding redundant computation.
"""

def minCoins(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1