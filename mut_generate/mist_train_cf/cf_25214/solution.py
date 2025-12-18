"""
QUESTION:
Create a function named `sortHashTableKeys` that sorts a given hashmap by its keys in ascending order. The function should take a hashmap with integer keys and string values as input and return a new sorted hashmap.
"""

def sortHashTableKeys(hash_table):
    """
    Sorts a given hashmap by its keys in ascending order.

    Args:
    hash_table (dict): A dictionary with integer keys and string values.

    Returns:
    dict: A new sorted dictionary.
    """
    # Create a new dictionary with the sorted keys
    sorted_hash_table = dict(sorted(hash_table.items()))
    return sorted_hash_table