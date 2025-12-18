"""
QUESTION:
Given a target amount of money `t` and an array of coin denominations `[d[0], d[1], ..., d[n]]`, write a function named `min_coins` to find the minimum number of coins needed to make up the amount `t`. The function should take two parameters: `t` and `d`, where `t` is an integer representing the target amount and `d` is a list of integers representing the coin denominations. The function should return an integer representing the minimum number of coins needed.
"""

def min_coins(t, d):
    """
    This function calculates the minimum number of coins needed to make up a certain amount of money.

    Parameters:
    t (int): The target amount of money.
    d (list): A list of coin denominations.

    Returns:
    int: The minimum number of coins needed to make up the amount t.
    """
    
    # Create a list to store the minimum number of coins needed for each amount from 0 to t
    F = [float('inf')] * (t + 1)
    
    # We need 0 coins to make up an amount of 0
    F[0] = 0
    
    # Iterate through all coin denominations
    for denom in d:
        # Iterate through all possible amounts from denom to t
        for amount in range(denom, t + 1):
            # Calculate the minimum number of coins needed for the current amount
            F[amount] = min(F[amount], 1 + F[amount - denom])
    
    # If no solution is found, return -1
    if F[t] == float('inf'):
        return -1
    
    # Return the minimum number of coins needed to make up the amount t
    return F[t]