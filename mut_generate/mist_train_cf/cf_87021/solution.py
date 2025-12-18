"""
QUESTION:
Write a function named `get_keys_with_value` that takes a dictionary and an integer value as input, and returns a list of string keys with the given value in sorted order. The function should assume that the input dictionary only contains string keys and integer values.
"""

def get_keys_with_value(dictionary, value):
    keys = []
    for key, val in dictionary.items():
        if val == value:
            keys.append(key)
    return sorted(keys)