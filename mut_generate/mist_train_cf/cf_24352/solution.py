"""
QUESTION:
Write a function `find_common_elements` that takes two lists `list1` and `list2` as input and returns a list of common elements between the two lists. The function should not include duplicate elements in the output list. 

Restrictions: Use list comprehension.
"""

def find_common_elements(list1, list2):
    """
    This function takes two lists as input and returns a list of common elements between the two lists.
    The function does not include duplicate elements in the output list.

    Args:
        list1 (list): The first input list.
        list2 (list): The second input list.

    Returns:
        list: A list of common elements between the two input lists.
    """
    return list(set([item1 for item1 in list1 for item2 in list2 if item1 == item2]))