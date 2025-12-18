"""
QUESTION:
Write a function `squared_lst` that takes a list of integers as input, squares each element, and returns a new list containing only the squared elements that are not divisible by 3.
"""

def squared_lst(lst):
    """
    This function takes a list of integers, squares each element, 
    and returns a new list containing only the squared elements that are not divisible by 3.

    Args:
        lst (list): A list of integers.

    Returns:
        list: A new list containing only the squared elements that are not divisible by 3.
    """
    return [i**2 for i in lst if (i**2)%3 != 0]