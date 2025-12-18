"""
QUESTION:
Create a function named `check_key` that takes a dictionary and a key as input. The dictionary has a maximum of 100 key-value pairs, where keys are alphanumeric strings between 1 and 10 characters long, are lowercase, and have unique positive integer values. The function should return the value corresponding to the key multiplied by 2 if the key is present in the dictionary; otherwise, return -1.
"""

def check_key(dictionary, key):
    """
    This function checks if a key is present in a given dictionary.
    If the key is present, it returns the corresponding value multiplied by 2.
    Otherwise, it returns -1.

    Args:
        dictionary (dict): A dictionary with alphanumeric keys and unique integer values.
        key (str): The key to be searched in the dictionary.

    Returns:
        int: The value corresponding to the key multiplied by 2 if the key is present; otherwise, -1.
    """
    if key in dictionary:
        return dictionary[key] * 2
    return -1