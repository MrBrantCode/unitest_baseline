"""
QUESTION:
Write a function called `sum_of_cubes` that calculates the sum of the cubes of all numbers from 1 to n, where n is a given integer. The function should take an integer n as input and return the sum of the cubes.
"""

def sum_of_cubes(n):
    """
    Calculates the sum of the cubes of all numbers from 1 to n.

    Args:
        n (int): The upper limit for calculating the sum of cubes.

    Returns:
        int: The sum of the cubes of all numbers from 1 to n.
    """
    return sum([num ** 3 for num in range(1, n+1)])