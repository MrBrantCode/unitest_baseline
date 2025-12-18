"""
QUESTION:
Write a function minNumCoins(v, c) that returns the minimum number of coins required to make a change for the value v using the available coin values in array c. The function should be able to handle various combinations of coin units and irregularities. The input value v is a positive integer and the array c contains positive integers representing the available coin values.
"""

def minNumCoins(v, c):
    """
    Returns the minimum number of coins required to make a change for the value v using the available coin values in array c.

    Args:
        v (int): A positive integer representing the value to make change for.
        c (list): A list of positive integers representing the available coin values.

    Returns:
        int: The minimum number of coins required to make a change for the value v.
    """

    # Create a table, minCoins, such that minCoins[i] stores the minimum number of coins required for value i.
    minCoins = [float('inf')] * (v + 1)
    
    # For value 0, we don't need any coins.
    minCoins[0] = 0
    
    # For each coin, with value c[j], go through the values c[j] to v.
    for j in range(len(c)):
        for i in range(c[j], v + 1):
            # Set minNumCoins[i] = min(minNumCoins[i], minNumCoins[i-c[j]] + 1).
            minCoins[i] = min(minCoins[i], minCoins[i - c[j]] + 1)
    
    # Return the minimum number of coins required to make a change for the value v.
    return minCoins[v] if minCoins[v] != float('inf') else -1  # Return -1 if not possible to make change.