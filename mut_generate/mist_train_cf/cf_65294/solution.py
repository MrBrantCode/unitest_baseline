"""
QUESTION:
Create a function called `custom_sort` that takes a 2D list of integers as input and returns the list sorted in descending order based on the secondary constituents of the minor arrays. If two or more secondary constituents are equal, the function should sort those minor arrays in descending order based on the sum of their elements.
"""

def custom_sort(arr):
    """
    Sorts a 2D list of integers in descending order based on the secondary constituents of the minor arrays.
    If two or more secondary constituents are equal, the function sorts those minor arrays in descending order based on the sum of their elements.

    Args:
        arr (list): A 2D list of integers.

    Returns:
        list: The sorted 2D list.
    """
    return sorted(arr, key=lambda x: (-x[1], -sum(x)))