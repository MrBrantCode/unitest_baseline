"""
QUESTION:
Create a function called `insert_item_at_end` that takes two parameters: an existing list and a new item to be inserted. The function must insert the new item at the end of the list without using the append() function or any built-in list methods or functions.
"""

def insert_item_at_end(existing_list, new_item):
    """
    Inserts a new item at the end of an existing list without using the append() function or any built-in list methods or functions.

    Args:
        existing_list (list): The original list to be modified.
        new_item: The item to be inserted at the end of the list.

    Returns:
        list: The updated list with the new item inserted at the end.
    """
    length = len(existing_list)
    new_list = [None] * (length + 1)
    for i in range(length):
        new_list[i] = existing_list[i]
    new_list[length] = new_item
    return new_list