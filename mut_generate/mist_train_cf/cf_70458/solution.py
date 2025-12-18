"""
QUESTION:
Create a function `is_subset` that takes two lists of items as input, removes duplicates from both lists, and checks if the first list is a subset of the second list. The function should return a boolean value indicating whether the first list is a subset of the second list. The input lists can contain duplicate items, but the function should ignore these duplicates during the subset check.
"""

def is_subset(list1, list2):
    """
    Checks if the first list is a subset of the second list after removing duplicates.

    Args:
        list1 (list): The first list of items.
        list2 (list): The second list of items.

    Returns:
        bool: True if list1 is a subset of list2, False otherwise.
    """
    set1 = set(list1)
    set2 = set(list2)
    return set1.issubset(set2)