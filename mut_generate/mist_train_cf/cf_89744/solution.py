"""
QUESTION:
Create a function `check_key` that takes a dictionary and a key as input, where the dictionary has lowercase alphanumeric keys with lengths between 1 and 10 characters, unique positive integer values, and a maximum of 100 key-value pairs. The function should return the corresponding value multiplied by 2 if the key is present in the dictionary; otherwise, it should return -1.
"""

def check_key(dictionary, key):
    """
    This function checks if a given key is present in a dictionary.
    If the key is present, it returns the corresponding value multiplied by 2.
    Otherwise, it returns -1.

    Parameters:
    dictionary (dict): A dictionary with lowercase alphanumeric keys and unique positive integer values.
    key (str): A key to be searched in the dictionary.

    Returns:
    int: The value corresponding to the key multiplied by 2 if found; otherwise, -1.
    """
    if key in dictionary:
        return dictionary[key] * 2
    return -1