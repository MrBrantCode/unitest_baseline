"""
QUESTION:
Write a function named `count_and_find_common_keys` that takes a dictionary with string keys and list of string values as input. Using nested loops, calculate the total number of keys and values in the dictionary and find the keys that are also present in their corresponding value lists. The function should return the total count of keys and values, and the list of common keys and values. The dictionary keys and values are case-sensitive.
"""

def count_and_find_common_keys(dictionary):
    """
    Calculate the total number of keys and values in the dictionary and find the keys that are also present in their corresponding value lists.

    Args:
    dictionary (dict): A dictionary with string keys and list of string values.

    Returns:
    tuple: A tuple containing the total count of keys and values, and the list of common keys and values.
    """
    count = 0
    common_keys_values = []

    for key, values in dictionary.items():
        count += 1
        for value in values:
            count += 1
            if key == value:
                common_keys_values.append(key)

    return count, common_keys_values