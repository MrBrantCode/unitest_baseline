"""
QUESTION:
Create a function `square_sum(array)` that takes an array of positive integers and returns the sum of the squares of its elements, excluding those squares that are divisible by 3. The function should not use any loops or conditional statements.
"""

def square_sum(array):
    """
    This function takes an array of positive integers and returns the sum of the squares of its elements, 
    excluding those squares that are divisible by 3.

    Args:
    array (list): A list of positive integers.

    Returns:
    int: The sum of the squares of the elements in the array, excluding those squares that are divisible by 3.
    """
    return sum(filter(lambda x: x % 3 != 0, map(lambda x: x ** 2, array)))