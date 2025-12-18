"""
QUESTION:
Given an array of arrays where each sub-array contains two identical elements, write a function named 'total_unique_items' that calculates the total number of unique elements in the array. The function should take a 2D list as input and return the difference between the total number of elements and the number of unique elements.
"""

def total_unique_items(array):
    """
    Calculate the total number of unique elements in a 2D list.

    Args:
        array (list): A 2D list where each sub-list contains two identical elements.

    Returns:
        int: The difference between the total number of elements and the number of unique elements.
    """
    total_items = len(sum(array, []))
    unique_items = len(set(sum(array, [])))
    return total_items - unique_items