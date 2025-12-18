"""
QUESTION:
Create a function called 'add_to_list' that adds a new item to an existing list without using the built-in 'append()' function or any other built-in list methods. The function should take two parameters: the existing list and the item to be added.
"""

def add_to_list(existing_list, new_item):
    """
    Adds a new item to an existing list without using the built-in 'append()' function or any other built-in list methods.

    Args:
        existing_list (list): The existing list to which the item is to be added.
        new_item (any): The item to be added to the existing list.

    Returns:
        list: The updated list with the new item.
    """
    return existing_list + [new_item]