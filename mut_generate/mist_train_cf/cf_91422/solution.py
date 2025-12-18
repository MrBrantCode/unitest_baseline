"""
QUESTION:
Write a function `get_value` that takes a JSON data object and a key as input, and returns the value associated with the given key. The key can contain dots to represent nested levels in the JSON data. For example, given the key "address.street", the function should return the value associated with "street" in the "address" object. The JSON data object can contain nested dictionaries and lists. If the key does not exist in the JSON data, the function should return None.
"""

import json

def get_value(json_data, key):
    # Split the key into nested levels
    nested_keys = key.split('.')
    
    # Initialize the current value as the entire JSON data
    current_value = json_data
    
    # Iterate through the nested keys
    for nested_key in nested_keys:
        # If the current value is a dictionary and the nested key exists
        if isinstance(current_value, dict) and nested_key in current_value:
            current_value = current_value[nested_key]
        # If the current value is a list and the nested key is an integer
        elif isinstance(current_value, list) and nested_key.isdigit():
            index = int(nested_key)
            if index < len(current_value):
                current_value = current_value[index]
            else:
                return None
        # If the key doesn't exist or the current value is not a dictionary or list
        else:
            return None
    
    # Return the final value
    return current_value