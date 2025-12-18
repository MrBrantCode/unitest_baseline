"""
QUESTION:
Retrieve the items from a dictionary in the order they were inserted. Create a function named `retrieve_items_in_order` that takes a dictionary as input and returns the items in the order they were inserted, considering Python versions 3.7 and above. The function should return the items as key-value pairs.
"""

def retrieve_items_in_order(input_dict):
    """
    Retrieve items from a dictionary in the order they were inserted.

    Args:
    input_dict (dict): The dictionary from which to retrieve items.

    Returns:
    list: A list of tuples containing the key-value pairs in the order they were inserted.
    """
    return list(input_dict.items())