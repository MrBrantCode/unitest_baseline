"""
QUESTION:
Write a function called `create_cubes_dict` that creates a dictionary containing the numbers 1 to n as the keys and their cubes as the values, where n is a given input. The function should have a time complexity of O(n) and should not use any built-in functions or libraries.
"""

def create_cubes_dict(n):
    """
    Creates a dictionary containing the numbers 1 to n as the keys and their cubes as the values.

    Args:
        n (int): The upper limit of the range of numbers.

    Returns:
        dict: A dictionary containing the numbers 1 to n as the keys and their cubes as the values.
    """
    cubes_dict = {}

    for num in range(1, n + 1):
        cubes_dict[num] = num ** 3

    return cubes_dict