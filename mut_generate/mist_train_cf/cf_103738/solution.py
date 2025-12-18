"""
QUESTION:
Create a function named `sort_and_remove_duplicates` that takes a list of integers as input. The function should sort the list in descending order and remove any duplicate elements.
"""

def sort_and_remove_duplicates(arr):
    """
    Sorts the input list of integers in descending order and removes any duplicate elements.

    Args:
        arr (list): A list of integers.

    Returns:
        list: A sorted list of unique integers in descending order.
    """
    return sorted(set(arr), reverse=True)