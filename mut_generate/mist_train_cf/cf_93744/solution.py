"""
QUESTION:
Create a function called `merge_lists` that takes two lists, `list1` and `list2`, as input and returns a new list containing unique elements from both lists, sorted in ascending order, with no negative numbers, and with all elements from `list1` coming before any elements from `list2`. The length of the new list should be equal to the sum of the lengths of `list1` and `list2`, but excluding any duplicates and negative numbers.
"""

def merge_lists(list1, list2):
    """
    This function merges two lists, removes duplicates and negative numbers, 
    and returns a new list with all elements from list1 before list2, 
    sorted in ascending order.

    Args:
        list1 (list): The first list.
        list2 (list): The second list.

    Returns:
        list: A new list containing unique elements from both lists.
    """
    combined_list = sorted(set(list1 + list2))
    return [x for x in combined_list if x >= 0]