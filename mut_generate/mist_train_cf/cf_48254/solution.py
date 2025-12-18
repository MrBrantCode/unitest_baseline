"""
QUESTION:
Write a function `min_coins` that determines the least quantity of coins required to accumulate a specified sum using a given collection of distinct coin values. The function should take two parameters: `coins` (a list of coin values) and `amount` (the target sum), and return the minimum number of coins needed. Assume that the coin values are positive and that the target sum is non-negative.
"""

def min_coins(coins, amount):
    # Create a list to store the minimum number of coins for each amount up to the target
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # 0 coins are needed to make 0 amount

    # Iterate over each coin value
    for coin in coins:
        # Iterate over each amount from the coin value to the target amount
        for i in range(coin, amount + 1):
            # Update the minimum number of coins for the current amount
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # Return the minimum number of coins for the target amount
    return dp[amount] if dp[amount] != float('inf') else -1