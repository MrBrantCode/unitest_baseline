"""
QUESTION:
Implement a function `retrieve_value` that retrieves the value of a specific key from a given dictionary, handling nested dictionaries. The function should return the value if the key is present, otherwise it should return None.
"""

def retrieve_value(dictionary, key):
    if key in dictionary:
        return dictionary[key]
    else:
        for value in dictionary.values():
            if isinstance(value, dict):
                nested_result = retrieve_value(value, key)
                if nested_result is not None:
                    return nested_result
    return None