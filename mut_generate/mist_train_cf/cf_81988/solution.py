"""
QUESTION:
Create a function called `minCoins` that determines the least quantity of coins required to accumulate a specific sum, given a collection of distinct coin denominations. The function should return the minimum number of coins needed to form the desired sum, or a notification if no combination of coins can sum to the target. The function should take two parameters: `coins` (a list of distinct coin denominations) and `amount` (the target sum).
"""

def minCoins(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1