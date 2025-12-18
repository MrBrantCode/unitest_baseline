"""
QUESTION:
Write a function named `remove_cubes` that takes a list of integers as input and returns a new list with integers that are not perfect cubes (i.e., exact cubes of an integer). The function should not modify the original list.
"""

def remove_cubes(lst):
    """
    This function takes a list of integers as input and returns a new list with integers that are not perfect cubes.
    
    Args:
        lst (list): A list of integers.
    
    Returns:
        list: A new list with integers that are not perfect cubes.
    """
    return [number for number in lst if number**(1./3.) != round(number**(1./3.))]