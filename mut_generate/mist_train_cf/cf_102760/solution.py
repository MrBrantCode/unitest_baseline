"""
QUESTION:
Create a function `create_cubes_dict` that generates a dictionary containing numbers from 1 to n as keys and their cubes as values. The function should have a time complexity of O(n) and should not use any built-in functions or libraries.
"""

def create_cubes_dict(n):
    """
    This function generates a dictionary containing numbers from 1 to n as keys and their cubes as values.

    Args:
        n (int): The upper limit for the range of numbers.

    Returns:
        dict: A dictionary with numbers as keys and their cubes as values.
    """
    cubes_dict = {}
    for num in range(1, n + 1):
        cubes_dict[num] = num ** 3
    return cubes_dict