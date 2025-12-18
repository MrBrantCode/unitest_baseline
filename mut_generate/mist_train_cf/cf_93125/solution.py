"""
QUESTION:
Implement a function named `retrieve_value` that retrieves the value of a specific key from a given dictionary, ignoring built-in dictionary methods. The function should handle nested dictionaries and return `None` if the key is not found. The function should take two parameters: `dictionary` and `key`.
"""

def retrieve_value(dictionary, key):
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