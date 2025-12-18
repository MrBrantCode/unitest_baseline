"""
QUESTION:
Create a function `deep_copy_2d_array` that creates a deep copy of a 2D array using only list comprehension and without using any built-in functions or methods. The input 2D array is a list of lists, and the function should have a time complexity of O(n^2).
"""

def deep_copy_2d_array(arr):
    """
    Creates a deep copy of a 2D array.

    Args:
        arr (list): A 2D array (list of lists) to be copied.

    Returns:
        list: A deep copy of the input 2D array.
    """
    return [row[:] for row in arr]