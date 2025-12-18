"""
QUESTION:
Write a function named `flatten_unique` that takes a two-dimensional list of integers as input, flattens the list into a one-dimensional list, and returns a new list containing unique elements.
"""

def flatten_unique(two_dimensional_list):
    """
    This function takes a two-dimensional list of integers as input, 
    flattens the list into a one-dimensional list, and returns a new 
    list containing unique elements.

    Args:
        two_dimensional_list (list): A 2D list of integers.

    Returns:
        list: A 1D list of unique integers.
    """
    return list(set([element for sublist in two_dimensional_list for element in sublist]))