"""
QUESTION:
Write a function `min_coins` that calculates the minimum number of coins required to make a certain amount using the denominations 1, 5, and 10. The function should return the minimum number of coins needed. The amount will be a positive integer.
"""

def min_coins(amount):
    """
    Calculate the minimum number of coins required to make a certain amount using the denominations 1, 5, and 10.

    Args:
        amount (int): The amount to make with coins.

    Returns:
        int: The minimum number of coins needed.
    """
    coins = [float('inf')] * (amount + 1)
    coins[0] = 0

    for coin in [1, 5, 10]:
        for i in range(coin, amount + 1):
            coins[i] = min(coins[i], coins[i - coin] + 1)

    return coins[amount] if coins[amount] != float('inf') else -1