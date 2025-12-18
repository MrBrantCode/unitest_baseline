"""
QUESTION:
Write a function named `add_item_to_list` that adds an item to a given list. The function should check if the item already exists in the list, if the item is of the correct data type, and if the list has reached its maximum capacity. The function should also allow adding an item at a specific position in the list and should return the updated list. The function should have a time complexity of O(n) and a space complexity of O(1). The function should take four parameters: the list, the item to be added, the index (optional), and the maximum capacity (optional).
"""

def add_item_to_list(lst, item, index=None, max_capacity=None):
    """
    Adds an item to a given list while checking for its existence, data type, and list capacity.

    Args:
        lst (list): The list to which the item is to be added.
        item: The item to be added to the list.
        index (int, optional): The index at which the item is to be added. Defaults to None.
        max_capacity (int, optional): The maximum capacity of the list. Defaults to None.

    Returns:
        list: The updated list with the item added, or an error message if any of the checks fail.
    """

    # Check if the item already exists in the list
    if item in lst:
        return "Item already exists in the list."

    # Check if the item is of the correct data type
    if not isinstance(item, type(lst[0])):
        return "Item is not of the correct data type."

    # Check if the list has reached its maximum capacity
    if max_capacity is not None and len(lst) >= max_capacity:
        return "List has reached its maximum capacity."

    # Add the item at the specified index or at the end of the list
    if index is not None:
        lst.insert(index, item)
    else:
        lst.append(item)

    return lst