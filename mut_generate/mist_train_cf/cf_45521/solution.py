"""
QUESTION:
Create a function `get_nested_key_value` that retrieves the value of a given key from a deeply nested dictionary. The dictionary can have other dictionaries as its values which can also contain dictionaries within them and so on. The function should be robust enough to handle any structure changes in the dictionary, such as a key going from a dictionary to a direct value. It should return the value of the key if found, and `None` otherwise.
"""

def get_nested_key_value(dictionary, key):
    """
    Retrieves the value of a given key from a deeply nested dictionary.
    
    Args:
        dictionary (dict): The dictionary to search in.
        key: The key to search for.
    
    Returns:
        The value of the key if found, and None otherwise.
    """
    if key in dictionary:
        return dictionary[key]
    elif any(isinstance(val, dict) for val in dictionary.values()):
        return next((get_nested_key_value(val, key) for val in dictionary.values() if isinstance(val, dict)), None)