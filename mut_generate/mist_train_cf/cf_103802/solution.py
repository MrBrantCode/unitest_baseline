"""
QUESTION:
Write a function `merge_sorted_unique` that takes two lists of equal lengths as input and returns a new list containing unique elements from both lists, sorted in ascending order.
"""

def merge_sorted_unique(list1, list2):
    """
    This function merges two lists, removes duplicates, and returns a new list 
    containing unique elements from both lists, sorted in ascending order.

    Args:
        list1 (list): The first list of elements.
        list2 (list): The second list of elements.

    Returns:
        list: A new list containing unique elements from both lists, sorted in ascending order.
    """
    return sorted(set(list1 + list2))