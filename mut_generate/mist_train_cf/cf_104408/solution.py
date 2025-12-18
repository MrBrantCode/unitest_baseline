"""
QUESTION:
Write a function `filter_items` that selects items from a collection based on the following conditions: price is greater than $10, quantity is less than 5, and color is not "red". The function should return a list of items that meet these conditions.
"""

def filter_items(items):
    """
    Selects items from a collection based on the following conditions: 
    price is greater than $10, quantity is less than 5, and color is not "red".

    Args:
        items (list): A list of dictionaries where each dictionary represents an item.

    Returns:
        list: A list of items that meet the conditions.
    """
    return [item for item in items if item['price'] > 10 and item['quantity'] < 5 and item['color'] != "red"]