"""
QUESTION:
Create a function `get_boolean_keys` that accepts a dictionary as an argument and returns all the key entries whose corresponding values are of type boolean or a list of boolean values. The function should handle complex dictionary structures where some values themselves are dictionaries and lists.
"""

def is_boolean(v):
    if isinstance(v, bool):
        return True
    elif isinstance(v, list) and all(isinstance(x, bool) for x in v):
        return True
    return False

def get_boolean_keys(d, parent_key=''):
    keys = []
    for k, v in d.items():
        new_key = f'{parent_key}.{k}' if parent_key else k
        if is_boolean(v):
            keys.append(new_key)
        elif isinstance(v, dict):
            keys.extend(get_boolean_keys(v, new_key))
        elif isinstance(v, list) and all(isinstance(x, dict) for x in v):
            for i, dict_value in enumerate(v):
                keys.extend(get_boolean_keys(dict_value, f'{new_key}[{i}]'))
    return keys