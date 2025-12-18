"""
QUESTION:
Write a function `compare(val1, val2)` that takes two arguments of any data type and returns `True` if both values are equal and of the same type, and `False` otherwise. The function should be able to handle multiple data types including strings, integers, floats, and booleans, as well as nested lists and dictionaries.
"""

def compare(val1, val2):
    if type(val1) != type(val2):
        return False

    if isinstance(val1, list):
        if len(val1) != len(val2):
            return False
        for item1, item2 in zip(val1, val2):
            if not compare(item1, item2):
                return False
        return True

    if isinstance(val1, dict):
        if len(val1) != len(val2):
            return False
        for key in val1:
            if key not in val2 or not compare(val1[key], val2[key]):
                return False
        return True

    return val1 == val2