"""
QUESTION:
Write a function `get_value` that retrieves the value associated with a given key from a JSON object. The function should support nested keys, where dots (.) represent nesting levels. If the key does not exist, the function should return `None`. The function should also handle cases where the key points to a value that is not a string, returning the value as is.
"""

def get_value(json_data, key):
    keys = key.split(".")
    value = json_data
    for k in keys:
        if isinstance(value, dict) and k in value:
            value = value[k]
        else:
            return None
    return value