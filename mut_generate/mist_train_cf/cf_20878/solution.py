"""
QUESTION:
Create a function named `create_dictionary` that takes two lists, `keys` and `values`, as input. The function should return a dictionary where the keys are from the `keys` list and the values are from the `values` list. If a key is an empty string or has a length greater than 10 characters, it should be ignored. If a value is a function, it should be executed and its return value used in the dictionary. The function should handle cases where the keys list contains duplicate values and the values list contains different data types.
"""

def create_dictionary(keys, values):
    result = {}
    for key, value in zip(keys, values):
        if isinstance(value, type(lambda: None)):
            value = value()
        if key != "" and len(key) <= 10:
            result[key] = value
    return result