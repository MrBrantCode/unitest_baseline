"""
QUESTION:
Write a function called minCoins that takes two parameters: coins (a list of coin denominations) and N (the total amount). Return the minimum number of coins necessary to make up the total amount N. The function should have a time complexity of O(MN), where M is the number of coin denominations.
"""

def minCoins(coins, N):
    dp = [float('inf')] * (N + 1)
    dp[0] = 0
    
    for coin in coins:
        for i in range(coin, N + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[N] if dp[N] != float('inf') else -1