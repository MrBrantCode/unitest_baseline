"""
QUESTION:
Write a function called `sort_in_descending_order` to sort a given array of strings in descending order. The function should take an array of strings as input and return the sorted array.
"""

def sort_in_descending_order(arr):
    """
    Sorts a given array of strings in descending order.
    
    Args:
        arr (list): The array of strings to be sorted.
    
    Returns:
        list: The sorted array in descending order.
    """
    return sorted(arr, reverse=True)