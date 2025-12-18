"""
QUESTION:
Write a function named `merge_lists` that takes two sorted lists as input and returns a new list that contains all elements from both lists, sorted in descending order. The input lists are sorted in descending order.
"""

def merge_lists(list1, list2):
    """
    Merge two sorted lists into one list in descending order.

    Args:
        list1 (list): The first sorted list in descending order.
        list2 (list): The second sorted list in descending order.

    Returns:
        list: A new list containing all elements from both input lists, sorted in descending order.
    """
    merged_list = list1 + list2
    merged_list.sort(reverse=True)
    return merged_list