"""
QUESTION:
Write a function `get_keys_with_value(dictionary, value)` to retrieve all keys from the given dictionary that correspond to a specific integer value, and return them in a sorted order. The dictionary only contains string keys and integer values.
"""

def entrance(dictionary, value):
    keys = []
    for key, val in dictionary.items():
        if val == value:
            keys.append(key)
    return sorted(keys)