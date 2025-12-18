"""
QUESTION:
Implement a function named `retrieve_value` that takes two parameters: a dictionary and a key. This function should return the value associated with the given key in the dictionary without using the built-in dictionary methods for key lookup. The function must handle nested dictionaries, where the key to be searched can be present in the outer dictionary or any of its nested dictionaries. If the key is not found, return None.
"""

def retrieve_value(dictionary, key):
    """
    This function retrieves the value associated with a given key in a dictionary.
    It handles nested dictionaries and does not use built-in dictionary methods for key lookup.
    
    Args:
    dictionary (dict): The dictionary to search in.
    key (any): The key to search for.
    
    Returns:
    any: The value associated with the key, or None if not found.
    """
    # Iterate over each key-value pair in the dictionary
    for k, v in dictionary.items():
        # If the current key is equal to the desired key
        if k == key:
            return v
        # If the current value is itself a dictionary
        elif isinstance(v, dict):
            # Recursively call the function on the nested dictionary
            result = retrieve_value(v, key)
            # If a non-None result is returned, return it
            if result is not None:
                return result
    # If the key is not found, return None
    return None