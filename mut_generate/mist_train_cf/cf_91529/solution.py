"""
QUESTION:
Create a function named `square_non_divisible_by_three` that takes a list of integers as input and returns a new list containing the square of each element, excluding any elements that are divisible by 3.
"""

def square_non_divisible_by_three(lst):
    """
    Returns a new list containing the square of each element in the input list,
    excluding any elements that are divisible by 3.
    
    Args:
        lst (list): A list of integers.
    
    Returns:
        list: A new list containing the square of each non-divisible element.
    """
    return [x**2 for x in lst if x % 3 != 0]