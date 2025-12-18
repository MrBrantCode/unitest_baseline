"""
QUESTION:
Write a function called `sum_of_pyramid` that calculates the total number of blocks required to build a pyramid of a given number of tiers. The pyramid has a specific structure where each tier has one block less than the previous tier. The function should take one argument `n` representing the number of tiers.
"""

def sum_of_pyramid(n):
    """
    Calculate the total number of blocks required to build a pyramid of a given number of tiers.

    Args:
    n (int): The number of tiers in the pyramid.

    Returns:
    int: The total number of blocks required to build the pyramid.
    """
    return n * (n + 1) // 2