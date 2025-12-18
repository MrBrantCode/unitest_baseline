"""
QUESTION:
Write a function named `add_to_beginning` that takes two parameters: `lst` and `element`. The function should return a new list with the `element` added to the beginning of `lst` without using any built-in list manipulation methods or functions.
"""

def add_to_beginning(lst, element):
    """
    Returns a new list with the element added to the beginning of lst without using any built-in list manipulation methods or functions.

    Args:
        lst (list): The original list.
        element: The element to be added to the beginning of the list.

    Returns:
        list: A new list with the element added to the beginning of lst.
    """
    new_list = [element]
    for item in lst:
        new_list.append(item)
    return new_list