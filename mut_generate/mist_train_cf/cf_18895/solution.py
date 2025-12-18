"""
QUESTION:
Write a function `get_value(dictionary, key)` that takes in a dictionary and a key as input and returns the value associated with that key in the dictionary. The dictionary can have an arbitrary number of nested levels. You can only use loops and conditional statements to navigate through the dictionary, and you cannot use any built-in functions or methods that directly extract values from dictionaries. If the key is not found, the function should return `None`.
"""

def get_value(dictionary, key):
    for k, v in dictionary.items():
        if k == key:
            return v
        elif isinstance(v, dict):
            result = get_value(v, key)
            if result is not None:
                return result
    return None