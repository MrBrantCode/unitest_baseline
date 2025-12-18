"""
QUESTION:
Write a function `coinChange` that takes two parameters: a list of distinct coin denominations and a total monetary value. The function should return the least number of coins required to achieve the total value. The function should handle edge cases, including when the total is zero, less than the smallest denomination, or a denomination itself. If no combination of coins can sum to the total, the function should return a value indicating it's impossible to make the change.
"""

def coinChange(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    return dp[amount] if dp[amount] != float('inf') else -1