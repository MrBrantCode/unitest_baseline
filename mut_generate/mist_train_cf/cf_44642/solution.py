"""
QUESTION:
Write a function named productOfExtremes that takes a list of integers as input and returns the product of the smallest and largest integers in the list.
"""

def productOfExtremes(lst):
    """
    This function takes a list of integers and returns the product of the smallest and largest integers in the list.

    Args:
        lst (list): A list of integers.

    Returns:
        int: The product of the smallest and largest integers in the list.
    """
    return min(lst) * max(lst)