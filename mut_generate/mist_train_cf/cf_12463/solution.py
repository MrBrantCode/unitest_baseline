"""
QUESTION:
Create a function named `square_non_divisible_by_three` that takes a list of integers as input and returns a new list containing the square of each element from the input list, excluding numbers that are divisible by 3.
"""

def square_non_divisible_by_three(arr):
    """
    This function takes a list of integers as input and returns a new list containing 
    the square of each element from the input list, excluding numbers that are divisible by 3.

    Args:
        arr (list): A list of integers.

    Returns:
        list: A new list containing the squares of elements excluding those divisible by 3.
    """
    return [x**2 for x in arr if x % 3 != 0]