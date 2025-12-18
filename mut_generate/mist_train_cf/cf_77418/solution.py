"""
QUESTION:
Write a function named `update_dict` that checks if a given key exists in a dictionary. If the key exists, update its value by concatenating the current value with the key. If the key does not exist, add the key with the value equal to its own name. The function should take two parameters: a dictionary and a key to check.
"""

def update_dict(dictionary, key):
    """
    Updates a dictionary by checking if a key exists. 
    If the key exists, its value is concatenated with the key. 
    If the key does not exist, it is added with its value equal to its own name.

    Args:
        dictionary (dict): The dictionary to be updated.
        key (str): The key to check and update.

    Returns:
        dict: The updated dictionary.
    """
    if key in dictionary:
        dictionary[key] += key
    else:
        dictionary[key] = key

    return dictionary