"""
QUESTION:
Write a function named `sortDescending` that sorts a given list of unique integers in descending order. The function should modify the original list and return it. The list may contain any number of unique integers.
"""

def sortDescending(lst):
    """
    Sorts a given list of unique integers in descending order.
    
    Args:
    lst (list): A list of unique integers.
    
    Returns:
    list: The sorted list in descending order.
    """
    lst.sort(reverse=True)
    return lst