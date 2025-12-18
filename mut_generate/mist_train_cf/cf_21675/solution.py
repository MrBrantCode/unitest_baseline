"""
QUESTION:
Create a function named `sort_and_remove_duplicates` that takes a list of integers as input, sorts the list in descending order, and removes any duplicate elements. The input list may contain negative numbers.
"""

def sort_and_remove_duplicates(lst):
    """
    Sorts the input list in descending order and removes duplicate elements.
    
    Args:
    lst (list): A list of integers.
    
    Returns:
    list: A sorted list in descending order with duplicates removed.
    """
    return sorted(set(lst), reverse=True)