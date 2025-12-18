"""
QUESTION:
Write a function `countWays(N, Coins)` that takes two inputs: `N`, a positive integer representing the amount of change, and `Coins`, a list of distinct, positive integers representing the coin denominations in ascending order. The function should return the number of ways to make a change of `N` with the given coin denominations. The function should be efficient and able to handle large values of `N` and `Coins`.
"""

def countWays(N, Coins):
    dp = [0] * (N+1)
    dp[0] = 1

    for coin in Coins:
        for i in range(coin, N+1):
            dp[i] += dp[i-coin]

    return dp[N]