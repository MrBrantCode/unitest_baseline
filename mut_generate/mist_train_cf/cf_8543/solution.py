"""
QUESTION:
Write a function 'insert_second_position' that takes two parameters: a list and an item. Insert the item at the second position in the list without using any built-in list methods or functions to add or insert the item. The original order of the list should be maintained except for the inserted item.
"""

def insert_second_position(lst, item):
    """
    Inserts an item at the second position in the list without using any built-in list methods or functions to add or insert the item.

    Args:
        lst (list): The input list.
        item: The item to be inserted.

    Returns:
        list: The modified list with the item inserted at the second position.
    """
    return lst[:1] + [item] + lst[1:]