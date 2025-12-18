"""
QUESTION:
Implement a function `findMinCoins(amount, coins)` that finds the minimum number of coins needed to make a given `amount` of money using a given set of `coins` denominations. The function should return a tuple containing the minimum number of coins and the combination of coins used to make the given amount of money. Assume an infinite supply of coins for each denomination.
"""

def findMinCoins(amount, coins):
    minCoins = [float('inf')] * (amount + 1)
    coinCombination = [[] for _ in range(amount + 1)]
    minCoins[0] = 0
    coinCombination[0] = []

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                if minCoins[i - coin] + 1 < minCoins[i]:
                    minCoins[i] = minCoins[i - coin] + 1
                    coinCombination[i] = coinCombination[i - coin] + [coin]

    return minCoins[amount], coinCombination[amount]