"""
QUESTION:
Implement a function named `construct_nested_dict` that constructs a nested dictionary structure given a list of key pairs where each primary key has a corresponding subordinate key. The function should take a list of tuples, where each tuple contains a primary key and a subordinate key, and return the constructed nested dictionary. The subordinate keys should map to empty dictionaries.
"""

def construct_nested_dict(key_pairs):
    """
    Construct a nested dictionary structure given a list of key pairs.

    Args:
        key_pairs (list): A list of tuples, where each tuple contains a primary key and a subordinate key.

    Returns:
        dict: The constructed nested dictionary.
    """
    dict_structure = {}
    for primary_key, subkey in key_pairs:
        dict_structure[primary_key] = {subkey: {}}
    return dict_structure