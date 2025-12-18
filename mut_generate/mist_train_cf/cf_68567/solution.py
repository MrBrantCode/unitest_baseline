"""
QUESTION:
Implement a function named `find_key` that retrieves the value(s) of a given key from any level of nesting in a tree-styled nested dictionary. If a key exists at multiple levels, the function should retrieve all associated values and return them as a list. If the key does not exist in the dictionary, the function should return None. The function should be able to handle KeyboardInterrupt exceptions.
"""

def find_key(nested_dict, target_key, values=None):
    if values is None:
        values = []
    try:
        for key, value in nested_dict.items():
            if key == target_key:
                values.append(value)
            if isinstance(value, dict):
                find_key(value, target_key, values)
        return values or None
    except KeyboardInterrupt:
        return None