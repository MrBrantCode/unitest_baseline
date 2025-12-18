"""
QUESTION:
Design a function called min_coins that determines the minimum number of coins required to reach a target amount using a given set of unique coin denominations. The function should take two parameters: an array of coin denominations and a target total amount. It should return the minimum number of coins needed to reach the target amount. Assume that it is always possible to make change for the target amount using the given coin denominations.
"""

def min_coins(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1