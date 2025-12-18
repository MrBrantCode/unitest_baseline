"""
QUESTION:
Write a function `get_all_keys(json_data, keys_list)` that takes JSON data and a list to store the keys, and returns a flattened list of all keys in the JSON data, regardless of nesting depth. The function must use recursion and not rely on built-in JSON parsing libraries. The input JSON data will always contain at least 3 key-value pairs. The function should be used to return the keys in reverse order.
"""

def get_all_keys(json_data, keys_list=None):
    """
    This function takes JSON data and a list to store the keys, 
    and returns a flattened list of all keys in the JSON data, 
    regardless of nesting depth, in reverse order.

    Args:
        json_data (dict or list): The input JSON data.
        keys_list (list, optional): The list to store the keys. Defaults to None.

    Returns:
        list: A flattened list of all keys in the JSON data in reverse order.
    """
    if keys_list is None:
        keys_list = []
    if isinstance(json_data, dict):
        for key in json_data.keys():
            keys_list.append(key)
            get_all_keys(json_data[key], keys_list)
    elif isinstance(json_data, list):
        for item in json_data:
            get_all_keys(item, keys_list)
    return keys_list[::-1]