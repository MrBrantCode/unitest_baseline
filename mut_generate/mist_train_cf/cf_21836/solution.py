"""
QUESTION:
Write a function `get_value(json_obj, key)` that takes a JSON object `json_obj` and a key `key` as input, and returns the value associated with the key if it exists in the JSON object. The function should recursively search for the key in nested objects and arrays within the JSON object.
"""

def get_value(json_obj, key):
    """
    Recursively searches for a key in a JSON object and returns the associated value.

    Args:
        json_obj (dict or list): The JSON object to search in.
        key (str): The key to search for.

    Returns:
        The value associated with the key if found, otherwise None.
    """
    if isinstance(json_obj, dict):
        if key in json_obj:
            return json_obj[key]
        for k, v in json_obj.items():
            if isinstance(v, (dict, list)):
                result = get_value(v, key)
                if result is not None:
                    return result
    elif isinstance(json_obj, list):
        for item in json_obj:
            result = get_value(item, key)
            if result is not None:
                return result