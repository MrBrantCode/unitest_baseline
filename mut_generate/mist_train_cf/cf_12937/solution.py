"""
QUESTION:
Create a function `merge_unique_elements` that takes two lists, `list_1` and `list_2`, as input and returns a list containing all unique elements from both lists. The function should remove any duplicate elements and maintain the original order is not required. The function should be able to handle lists containing integers.
"""

def merge_unique_elements(list_1, list_2):
    """
    This function merges two lists, removes duplicates, and returns the resulting list.

    Args:
        list_1 (list): The first list to be merged.
        list_2 (list): The second list to be merged.

    Returns:
        list: A list containing unique elements from both input lists.
    """
    return list(set(list_1 + list_2))