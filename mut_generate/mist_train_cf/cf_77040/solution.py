"""
QUESTION:
Construct a function `find_boolean_keys` that takes a single-layer dictionary as input and returns a list of keys corresponding to values that are of type boolean.
"""

def find_boolean_keys(input_dict):
    boolean_keys = [key for key, value in input_dict.items() if type(value) == bool]
    return boolean_keys