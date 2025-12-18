"""
QUESTION:
Create a function called `get_item_at_index` that takes a list and an index as input, and returns the item at the specified index without using built-in list indexing or slicing methods. The function should only use a loop and basic list manipulation techniques.
"""

def get_item_at_index(lst, index):
    """
    Returns the item at the specified index in the given list.
    
    Args:
        lst (list): The input list.
        index (int): The index of the item to retrieve.
    
    Returns:
        The item at the specified index, or None if the index is out of range.
    """
    counter = 0
    item_at_index = None

    for item in lst:
        if counter == index:
            item_at_index = item
            break
        counter += 1

    return item_at_index