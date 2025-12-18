"""
QUESTION:
Calculate the sum of cubes of even numbers from 1 to n, where n is a positive integer. The function should be named 'sum_of_cubes_of_even_numbers' and it should take one argument, n. The function should return the sum of cubes of even numbers from 1 to n.
"""

def sum_of_cubes_of_even_numbers(n):
    """
    Calculate the sum of cubes of even numbers from 1 to n.

    Args:
        n (int): A positive integer.

    Returns:
        int: The sum of cubes of even numbers from 1 to n.
    """
    sum_cubes = 0
    for i in range(2, n + 1, 2):
        sum_cubes += i ** 3
    return sum_cubes