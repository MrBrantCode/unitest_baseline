"""
QUESTION:
Implement the function `minCoins(coins, target)` that finds the minimum number of coins needed to make up the target amount using the given coin denominations. The function should take two parameters: 
- `coins`, a list of positive integers representing the available coin denominations, 
- `target`, a positive integer representing the target amount of money. 

The function should return the minimum number of coins needed to make up the target amount. If it is not possible to make up the target amount using the given coin denominations, return -1.
"""

def minCoins(coins, target):
    dp = [float('inf')] * (target + 1)
    dp[0] = 0  
    for coin in coins:
        for amount in range(coin, target + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)
    if dp[target] == float('inf'):
        return -1
    else:
        return dp[target]