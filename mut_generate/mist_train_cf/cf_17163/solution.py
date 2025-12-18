"""
QUESTION:
Implement a function minimumCoins that finds the minimum number of coins needed to make a given amount of money using a given set of coin denominations. The function should take two parameters: an integer amount representing the amount of money to be made, and a list coins representing the available coin denominations. The function should return an integer representing the minimum number of coins needed. Assume that there is an infinite supply of coins for each denomination.
"""

def minCoins(amount, coins):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount]