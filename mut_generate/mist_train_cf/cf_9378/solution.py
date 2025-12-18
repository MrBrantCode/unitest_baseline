"""
QUESTION:
Write a function called `remove_element` that takes a list `lst` and an element as input, and returns a new list with all occurrences of the given element removed. The function should achieve this in O(n) time complexity, where n is the length of the list. The original list should not be modified.
"""

def remove_element(lst, element):
    """
    Removes all occurrences of a given element from a list in O(n) time complexity.

    Args:
        lst (list): The input list.
        element: The element to be removed.

    Returns:
        list: A new list with all occurrences of the given element removed.
    """
    return [i for i in lst if i != element]