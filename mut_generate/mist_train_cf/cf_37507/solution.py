"""
QUESTION:
Write a function `minCoins(coins, amount)` where `coins` is a list of positive integers representing the available coin denominations and `amount` is a positive integer representing the target amount. Return the minimum number of coins needed to make up the amount, or -1 if it is not possible.
"""

def minCoins(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  

    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin and dp[i - coin] != float('inf'):
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1