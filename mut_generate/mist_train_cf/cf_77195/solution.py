"""
QUESTION:
Create a function `add_item` that generates unique identification numbers and associates each of them with an individual item. The function should ensure the uniqueness of items. The input will be a list of items and the function should output the unique ID for each item.
"""

def add_item(items):
    """
    Generates unique identification numbers and associates each of them with an individual item.
    
    Args:
    items (list): A list of items.
    
    Returns:
    dict: A dictionary where keys are unique IDs and values are the corresponding items.
    """
    unique_items = {}
    index = 1
    for item in items:
        if item not in unique_items.values():
            unique_items[index] = item
            index += 1
    return unique_items