"""
QUESTION:
Write a function `find_common_kv_pairs` that takes a list of dictionaries `dicts` as input and returns a dictionary containing the key-value pairs that are common to all dictionaries in the list. Each dictionary can have any number of key-value pairs, and the keys-values are not limited to a specific type. Assume all values in the dictionaries are hashable and can be used in a set. The function should be efficient in terms of space and time complexity.
"""

def find_common_kv_pairs(dicts):
    """
    This function takes a list of dictionaries as input and returns a dictionary containing 
    the key-value pairs that are common to all dictionaries in the list.

    Args:
        dicts (list): A list of dictionaries.

    Returns:
        dict: A dictionary containing the common key-value pairs.
    """
    # Check if the list of dictionaries is empty
    if not dicts:
        return {}

    # Initialize common with the key-value pairs of the first dictionary
    common = set(dicts[0].items())

    # Iterate over the remaining dictionaries to find the common key-value pairs
    for d in dicts[1:]:
        common = common & set(d.items())

    # Convert the set of common key-value pairs back to a dictionary
    return dict(common)