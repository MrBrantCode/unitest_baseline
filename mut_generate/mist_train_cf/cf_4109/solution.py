"""
QUESTION:
Write a function `get_value(dictionary, key)` that takes in a dictionary and a key as input and returns the value associated with the key in the dictionary. The dictionary can have an arbitrary number of nested levels and may contain values that are strings, integers, lists, and other dictionaries. The function should be able to extract the correct value regardless of its position within the dictionary. The function cannot use any built-in functions or methods that directly extract values from dictionaries, such as the `get()` method or dictionary indexing. Instead, it should only use loops and conditional statements to navigate through the dictionary.
"""

def get_value(dictionary, key):
    if isinstance(dictionary, dict):
        for k, v in dictionary.items():
            if k == key:
                return v
            elif isinstance(v, dict):
                result = get_value(v, key)
                if result is not None:
                    return result
            elif isinstance(v, list):
                for item in v:
                    result = get_value(item, key)
                    if result is not None:
                        return result
    return None