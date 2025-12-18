"""
QUESTION:
Write a function called `combine_lists` that takes two lists of strings as input and returns a new list that contains all unique strings from both lists, without any duplicates. The function should be able to handle lists of any size.
"""

def combine_lists(list1, list2):
    """
    Combines two lists of strings into one list with unique values.

    Args:
        list1 (list): The first list of strings.
        list2 (list): The second list of strings.

    Returns:
        list: A new list containing all unique strings from both input lists.
    """
    return list(set(list1 + list2))