"""
QUESTION:
Create a function called `merge_dicts_interleaved` that merges two dictionaries by interleaving their key-value pairs. The function should return a new dictionary where the first key-value pair comes from the first dictionary, the second key-value pair comes from the second dictionary, and so on. If the dictionaries are of unequal lengths, the remaining key-value pairs from the longer dictionary should be appended to the end of the new dictionary. The function assumes that dictionary order is guaranteed (i.e., it is designed for Python 3.6 and later).
"""

def merge_dicts_interleaved(dict1, dict2):
    """
    Merge two dictionaries by interleaving their key-value pairs.

    Args:
        dict1 (dict): The first dictionary.
        dict2 (dict): The second dictionary.

    Returns:
        dict: A new dictionary with the key-value pairs interleaved.
    """
    result = {}

    # Interleave key-value pairs from both dictionaries
    for (k1, v1), (k2, v2) in zip(dict1.items(), dict2.items()):
        result[k1] = v1
        result[k2] = v2

    # Append remaining items from the longer dictionary
    if len(dict1) > len(dict2):
        for k, v in list(dict1.items())[len(dict2):]:
            result[k] = v
    elif len(dict2) > len(dict1):
        for k, v in list(dict2.items())[len(dict1):]:
            result[k] = v

    return result