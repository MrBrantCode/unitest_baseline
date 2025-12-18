"""
QUESTION:
Write a Python function named `amalgamate_dicts` that takes two dictionaries as input and returns a set containing their unique key-value pairs, treating pairs with the same key but different values as unique elements.
"""

def amalgamate_dicts(dict1, dict2):
    """
    Amalgamates two dictionaries into a set of unique key-value pairs.

    Args:
        dict1 (dict): The first dictionary.
        dict2 (dict): The second dictionary.

    Returns:
        set: A set containing the unique key-value pairs from both dictionaries.
    """
    return set(dict1.items()).union(set(dict2.items()))