"""
QUESTION:
Implement a function `add_to_dictionary` that adds a key-value pair to a dictionary. The function should enforce the following rules:
- The key must be a string with a length between 1 and 10 characters.
- The key must be alphanumeric.
- The value must be a positive integer.
- The dictionary can contain a maximum of 100 key-value pairs.

The function should return or print a message indicating whether the key-value pair was added successfully or not.
"""

def add_to_dictionary(dictionary, key, value):
    """
    Adds a key-value pair to a dictionary while enforcing certain rules.

    Args:
    dictionary (dict): The dictionary to which the key-value pair is added.
    key (str): The key to be added.
    value (int): The value associated with the key.

    Returns:
    dict: The updated dictionary.
    """
    if (len(key) > 0 and len(key) <= 10) and key.isalnum() and value > 0 and len(dictionary) < 100:
        dictionary[key] = value
        print("Key-value pair added successfully.")
    else:
        print("Invalid key-value pair.")
    return dictionary