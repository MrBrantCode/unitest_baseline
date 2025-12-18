"""
QUESTION:
Implement a function `findMinCoins(amount, coins)` that finds the minimum number of coins needed to make a given amount of money using a given set of coin denominations and returns the combination of coins used to make the given amount of money. Assume that there is an infinite supply of coins for each denomination.
"""

def entrance(amount, coins):
    # Create a list to store the minimum number of coins needed for each amount
    minCoins = [float('inf')] * (amount + 1)
    # Create a list to store the combination of coins used for each amount
    coinCombination = [[]] * (amount + 1)

    # Base case: 0 coins needed to make 0 amount
    minCoins[0] = 0
    coinCombination[0] = []

    # Iterate through all possible amounts up to the given amount
    for i in range(1, amount + 1):
        # Try all possible coin denominations
        for coin in coins:
            # Check if the current coin can be used to make the current amount
            if coin <= i:
                # Check if using this coin would result in fewer coins needed
                if minCoins[i - coin] + 1 < minCoins[i]:
                    # Update the minimum number of coins needed for the current amount
                    minCoins[i] = minCoins[i - coin] + 1
                    # Update the combination of coins used for the current amount
                    coinCombination[i] = coinCombination[i - coin] + [coin]

    # Return the minimum number of coins needed and the combination of coins used for the given amount
    return minCoins[amount], coinCombination[amount]