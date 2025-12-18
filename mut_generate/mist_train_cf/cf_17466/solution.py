"""
QUESTION:
Implement a function `reverse_dict` that takes a dictionary as input, where all keys and values are strings or dictionaries of strings. The function should return a new dictionary with the same structure as the input, but with all strings reversed. The function should handle nested dictionaries and prevent infinite loops caused by circular references.
"""

def reverse_dict(dictionary):
    reversed_dict = {}
    visited_dicts = set()

    def reverse_nested_dict(nested_dict):
        if id(nested_dict) in visited_dicts:
            return nested_dict

        visited_dicts.add(id(nested_dict))

        reversed_nested_dict = {}
        for key, value in nested_dict.items():
            if isinstance(value, dict):
                reversed_nested_dict[key[::-1]] = reverse_nested_dict(value)
            else:
                reversed_nested_dict[key[::-1]] = value[::-1]

        return reversed_nested_dict

    for key, value in dictionary.items():
        if isinstance(value, dict):
            reversed_dict[key[::-1]] = reverse_nested_dict(value)
        else:
            reversed_dict[key[::-1]] = value[::-1]

    return reversed_dict