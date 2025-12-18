"""
QUESTION:
Write a function `most_frequent` that takes a dictionary as input and returns the key with the highest value, assuming the dictionary contains at least one key-value pair and values are non-negative integers. If there are multiple keys with the same highest value, return any of them.
"""

def most_frequent(my_dict):
    """
    Returns the key with the highest value in the given dictionary.

    Args:
        my_dict (dict): A dictionary containing at least one key-value pair with non-negative integer values.

    Returns:
        The key with the highest value.
    """
    return max(my_dict, key=my_dict.get)