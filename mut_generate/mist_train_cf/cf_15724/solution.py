"""
QUESTION:
Create a function `merge_lists(list1, list2)` that takes two sorted lists as input and returns a new list containing all elements from both lists, sorted in descending order. The input lists are already sorted in descending order. The function should not modify the original input lists.
"""

def merge_lists(list1, list2):
    """
    Merge two sorted lists into a new list, sorted in descending order.

    Args:
        list1 (list): The first sorted list.
        list2 (list): The second sorted list.

    Returns:
        list: A new list containing all elements from both lists, sorted in descending order.
    """
    return sorted(list1 + list2, reverse=True)