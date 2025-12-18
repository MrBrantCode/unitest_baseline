"""
QUESTION:
Implement a function called `find_minimum` that takes a list as an argument. The function should find and return the minimum value in the list using recursion, without using any built-in functions or libraries. The function should be able to handle both numerical and non-numerical elements, as well as lists with duplicate minimum values. The function should return `None` if the list is empty.
"""

def find_minimum(lst):
    """
    This function finds and returns the minimum value in a list using recursion.
    
    Args:
        lst (list): A list containing elements of any type.
    
    Returns:
        The minimum value in the list, or None if the list is empty.
    """
    if len(lst) == 0:
        return None
    elif len(lst) == 1:
        return lst[0]
    else:
        min_rest = find_minimum(lst[1:])
        return lst[0] if lst[0] < min_rest else min_rest