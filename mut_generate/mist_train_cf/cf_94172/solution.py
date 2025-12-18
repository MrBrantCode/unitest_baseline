"""
QUESTION:
Write a function `store_key_value` that takes a dictionary, a string key containing only alphabetic characters, and a positive integer value as input. The function should store the key-value pair in the dictionary. If the key already exists, update the value and increment a counter that keeps track of the number of times the key has been updated. The function should not return any value.
"""

def store_key_value(dictionary, key, value):
    """
    Stores a key-value pair in the dictionary and tracks the number of updates.

    Args:
        dictionary (dict): The dictionary to store the key-value pair.
        key (str): A string key containing only alphabetic characters.
        value (int): A positive integer value.

    Returns:
        None
    """
    # Check if key is a string containing only alphabetic characters
    if not key.isalpha():
        print("Invalid key! The key must be a string containing only alphabetic characters.")
        return

    # Check if value is a positive integer
    if not isinstance(value, int) or value <= 0:
        print("Invalid value! The value must be a positive integer.")
        return

    # Check if the key already exists in the dictionary
    if key in dictionary:
        dictionary[key] = value
        dictionary[key+"_updates"] = dictionary.get(key+"_updates", 0) + 1
    else:
        dictionary[key] = value
        dictionary[key+"_updates"] = 1