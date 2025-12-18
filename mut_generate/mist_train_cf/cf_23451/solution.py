"""
QUESTION:
Write a function `delete_items_with_prefix` that takes a dictionary as input and deletes all items whose keys start with a specified prefix "item". The function should return the updated dictionary.
"""

def delete_items_with_prefix(input_dict):
    """
    Deletes all items from a dictionary whose keys start with a specified prefix "item".
    
    Args:
    input_dict (dict): The input dictionary to be updated.
    
    Returns:
    dict: The updated dictionary after deletion.
    """
    return {key: value for key, value in input_dict.items() if not key.startswith('item')}