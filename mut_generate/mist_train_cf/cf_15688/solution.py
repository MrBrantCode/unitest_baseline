"""
QUESTION:
Implement a function named find_index that takes two parameters: a list and an item. Write your own logic to search for the item in the list and return its index. If the item is not found in the list, the function should return -1. The function should not use any built-in index() function or other built-in functions to find the index.
"""

def find_index(lst, item):
    """
    Searches for an item in a list and returns its index.

    Args:
        lst (list): The list to search in.
        item: The item to search for.

    Returns:
        int: The index of the item if found, -1 otherwise.
    """
    for i in range(len(lst)):
        if lst[i] == item:
            return i
    return -1