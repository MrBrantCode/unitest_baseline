"""
QUESTION:
Write a function `get_change(m)` that takes an integer `m` as input and returns the minimum number of coins needed to change the input value into coins with denominations 1, 3, and 4. Assume that you have an infinite number of coins of each denomination and that you can use each denomination any number of times.
"""

def get_change(m):
    min_coins = [0] * (m + 1)
    denominations = [1, 3, 4]

    for i in range(1, m + 1):
        min_coins[i] = float('inf')
        for coin in denominations:
            if i >= coin:
                num_coins = min_coins[i - coin] + 1
                if num_coins < min_coins[i]:
                    min_coins[i] = num_coins

    return min_coins[m]