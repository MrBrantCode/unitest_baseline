"""
QUESTION:
Create a function named `minCoins` that takes in a list of distinct currency denominations and a target amount. The function should return the minimum number of coins required to reach the target amount using the given denominations. If it is impossible to achieve the desired amount, return -1. The function should use dynamic programming principles to solve the problem efficiently.
"""

def minCoins(denominations, amount):
    # Create a memoization list with amount + 1 in size (from 0 to amount)
    memo = [float('inf')] * (amount + 1)
    memo[0] = 0  # When the amount is 0, the minimum number of coins is also 0

    # For each denomination, calculate the minimum number of coins required for every amount
    for coin in denominations:
        for curr_amount in range(coin, amount + 1):
            # Check if the denomination can be used to get a better result
            memo[curr_amount] = min(memo[curr_amount], 1 + memo[curr_amount - coin])

    # Return -1 if no combination of coins exists to reach the given amount
    return -1 if memo[amount] == float('inf') else memo[amount]