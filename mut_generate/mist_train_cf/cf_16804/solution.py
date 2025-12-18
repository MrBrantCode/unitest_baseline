"""
QUESTION:
Write a function `countChange(N, Coins)` that calculates the number of ways to make a change of `N` using the given `Coins`. The function should take two parameters: `N`, the amount of change to be made, and `Coins`, a list of coin denominations. The `Coins` list may contain duplicate denominations and is guaranteed to be non-empty, contain only positive integers, and be in ascending order.
"""

def entrance(N, Coins):
    dp = [0] * (N + 1)
    dp[0] = 1

    for coin in Coins:
        for i in range(coin, N + 1):
            dp[i] += dp[i - coin]

    return dp[N]