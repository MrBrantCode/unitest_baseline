"""
QUESTION:
Write a function named `get_value` that takes in a dictionary and a key. The function should return the value associated with the given key from the dictionary. The dictionary can have an arbitrary number of nested levels and can contain values that are strings, integers, lists, or other dictionaries. The function should be able to extract the correct value regardless of its position within the dictionary. The function cannot use any built-in functions or methods that directly extract values from dictionaries, such as the `get` method or the `[]` operator, and should instead use loops and conditional statements to navigate through the dictionary.
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