"""
QUESTION:
Compute the number of ways to make a change of N using the given distinct and ascending coin denominations. Implement a function `numWays(N, Coins)` to calculate this, where N is a positive integer and Coins is an array of distinct and ascending positive integers.
"""

def make_change(N, Coins):
    dp = [0] * (N + 1)
    dp[0] = 1
    
    for coin in Coins:
        for i in range(coin, N + 1):
            dp[i] += dp[i - coin]
    
    return dp[N]