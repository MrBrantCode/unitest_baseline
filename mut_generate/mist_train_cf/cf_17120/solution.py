"""
QUESTION:
Write a recursive function `get_keys_reverse(json_data)` that takes a JSON object as input, which may contain nested dictionaries and lists, and returns a list of all keys in the JSON object in reverse order.
"""

def get_keys_reverse(json_data):
    if isinstance(json_data, dict):
        keys = list(json_data.keys())
        keys.reverse()
        sub_keys = []
        for key in keys:
            sub_keys.extend(get_keys_reverse(json_data[key]))
        return sub_keys + keys
    elif isinstance(json_data, list):
        sub_keys = []
        for item in json_data:
            sub_keys.extend(get_keys_reverse(item))
        return sub_keys
    else:
        return []