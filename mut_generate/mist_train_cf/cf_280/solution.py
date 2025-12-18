"""
QUESTION:
Create a function called `get_item_at_index_2` that extracts the item at index 2 from a given list without using built-in list indexing or slicing methods, the length of the list, or the range function. The function should use a loop and basic list manipulation techniques.
"""

def get_item_at_index_2(lst):
    """
    Extracts the item at index 2 from a given list without using built-in list indexing or slicing methods.
    
    Args:
        lst (list): The input list.
    
    Returns:
        The item at index 2 in the list.
    """
    item_at_index_2 = None
    count = 0

    for item in lst:
        if count == 2:
            item_at_index_2 = item
            break
        count += 1

    return item_at_index_2