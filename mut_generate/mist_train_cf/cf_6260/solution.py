"""
QUESTION:
Create a function `remove_duplicates` that takes a list as input and returns a new list that contains the same elements, excluding any duplicates, without using built-in Python functions or methods for duplicate removal or list manipulation. The function should have a time complexity less than O(n^2) and a space complexity of O(1).
"""

def remove_duplicates(lst):
    """
    Create a copy of a given list and exclude any duplicate elements.
    
    Args:
    lst (list): The input list that may contain duplicate elements.
    
    Returns:
    list: A new list containing the same elements, excluding any duplicates.
    """
    return [x for i, x in enumerate(lst) if x not in lst[:i]]