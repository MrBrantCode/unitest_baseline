"""
QUESTION:
Implement a function named `retrieve_value` that takes two parameters: `dictionary` and `key`. This function should retrieve the value of the given `key` from the `dictionary`, handling nested dictionaries. If the `key` is found, return its corresponding value; otherwise, return `None`. The function should not raise any exceptions if the `key` is not present in the `dictionary`.
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