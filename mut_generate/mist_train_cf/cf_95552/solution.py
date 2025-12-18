"""
QUESTION:
Write a function `find_common_items` that takes two lists as input and returns a new list containing the common items between the two lists. The function should handle lists of any length and items of any data type, including nested lists, and return the common items in a flattened list.
"""

def flatten_list(lst):
    """Helper function to flatten a list."""
    flattened_list = []
    for item in lst:
        if isinstance(item, list):
            flattened_list.extend(flatten_list(item))
        else:
            flattened_list.append(item)
    return flattened_list

def find_common_items(list1, list2):
    """Returns a list of common items between two lists."""
    list1 = flatten_list(list1)
    list2 = flatten_list(list2)
    common_items = [item for item in list1 if item in list2]
    return common_items