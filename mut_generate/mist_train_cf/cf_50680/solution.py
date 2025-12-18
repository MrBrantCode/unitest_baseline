"""
QUESTION:
Create a Python function `get_value(json_obj, key_path)` that retrieves values from a given JSON object `json_obj` using a specific path of keys `key_path`. The function should handle nested JSON objects and arrays, treating arrays as key-value pairs with indices as keys. The `key_path` should be a string with keys separated by dots for nested objects and `[]` for array indices. The function should return the value at the specified path in the JSON object.
"""

def get_value(json_obj, key_path):
    keys = key_path.split('.')
    value = json_obj
    for key in keys:
        if '[' in key and ']' in key:  
            key, index = key.split('[')
            index = int(index.strip(']'))
            value = value[key][index]
        else:
            value = value[key]
    return value