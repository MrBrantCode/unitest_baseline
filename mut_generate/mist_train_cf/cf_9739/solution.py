"""
QUESTION:
Design a function `search_item_indices` that takes two parameters: a list `list_items` and an item `item_to_search`. The function should return a list of indices where `item_to_search` appears in `list_items`. If `item_to_search` is not found in `list_items`, return an empty list. The function should have a time complexity of O(n), where n is the length of `list_items`.
"""

def search_item_indices(list_items, item_to_search):
    """
    Searches for the given item in the list and returns the indices of all occurrences.

    Args:
        list_items (list): The list to search in.
        item_to_search: The item to search for.

    Returns:
        list: A list of indices where item_to_search appears in list_items. If item_to_search is not found, returns an empty list.
    """
    indices = []
    for i in range(len(list_items)):
        if list_items[i] == item_to_search:
            indices.append(i)
    return indices