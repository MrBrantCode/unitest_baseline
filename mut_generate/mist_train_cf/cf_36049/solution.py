"""
QUESTION:
Write a function `count_ways_to_make_change(coins, amount)` that calculates the number of unique ways to make change for a given amount using the provided coins, where an infinite number of coins of each denomination is available. The function should take in two parameters: `coins`, a list of integers representing different coin denominations, and `amount`, an integer representing the total amount for which change needs to be made. The function should return an integer representing the number of unique ways to make change for the given amount using the provided coins.
"""

def count_ways_to_make_change(coins, amount):
    dp = [0] * (amount + 1)
    dp[0] = 1  # Base case: 1 way to make change for 0

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]

    return dp[amount]