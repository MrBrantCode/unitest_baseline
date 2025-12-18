"""
QUESTION:
Write a function called `get_value` that takes in a dictionary and a key, and returns the value associated with that key. The dictionary can be nested and the function should be able to traverse through the dictionary recursively to find the desired key. The function should not use any built-in functions or methods that directly extract values from dictionaries, such as the `dict.get()` method or dictionary indexing with square brackets `[]`. Instead, it should only use loops and conditional statements to navigate through the dictionary.
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