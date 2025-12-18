"""
QUESTION:
Implement a function `get_all_keys(json_data)` that recursively traverses the given JSON data and returns a list of all the keys in reverse order. The JSON data can contain at least 3 key-value pairs and may have nested structures. The function should not use any built-in JSON parsing libraries.
"""

def entrance(json_data):
    def get_all_keys(json_data, keys_list):
        if isinstance(json_data, dict):
            for key in json_data.keys():
                keys_list.append(key)
                get_all_keys(json_data[key], keys_list)
        elif isinstance(json_data, list):
            for item in json_data:
                get_all_keys(item, keys_list)

    keys_list = []
    get_all_keys(json_data, keys_list)
    return keys_list[::-1]