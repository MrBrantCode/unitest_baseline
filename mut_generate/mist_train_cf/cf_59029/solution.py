"""
QUESTION:
Write a function named `find_last_index` that takes a list and an item as input, and returns the last index of the item in the list. If the item is not found, return a message indicating that the item is not in the list. Do not use Python's built-in 'rindex' or 'list.reverse' methods.
"""

def find_last_index(lst, item):
    """
    Returns the last index of the item in the list.
    If the item is not found, returns a message indicating that the item is not in the list.

    Args:
        lst (list): The list to search in.
        item: The item to search for.

    Returns:
        int or str: The last index of the item if found, otherwise a message indicating the item is not in the list.
    """
    for i in range(len(lst)-1, -1, -1):
        if lst[i] == item:
            return i
    return f'Item {item} is not in the list'