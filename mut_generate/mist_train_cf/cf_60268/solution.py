"""
QUESTION:
Create a function `create_nested_dict(keys, values)` that takes two lists of tuples, `keys` and `values`, and returns a nested dictionary where each key from `keys` is mapped to a sub-dictionary containing the corresponding value from `values`. Also, implement a function `deep_search(d, target_key, target_value)` that performs a deep search for a given key-value pair within the dictionary and returns True if found, False otherwise. The key in the target key-value pair can be a sub-key, and the value can be a tuple of values.
"""

def create_nested_dict(keys, values):
    """Creates a nested dictionary from given keys and values."""
    return {k[0]: {k[1]: v} for k, v in zip(keys, values)}

def entrance(d, target_key, target_value):
    """Performs a deep search for a given key-value pair within the dictionary."""
    for key, value in d.items():
        if key == target_key and value == target_value:
            return True
        elif isinstance(value, dict):
            if entrance(value, target_key, target_value):
                return True
    return False