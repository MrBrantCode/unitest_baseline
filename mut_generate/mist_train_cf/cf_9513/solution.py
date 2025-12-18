"""
QUESTION:
Write a function named `compare_json` that compares two nested JSON objects and returns `True` if they are identical and `False` otherwise. The function should handle JSON objects with multiple nested levels and different data types, including dictionaries and lists.
"""

def compare_json(obj1, obj2):
    if type(obj1) != type(obj2):
        return False

    if isinstance(obj1, dict):
        if len(obj1) != len(obj2):
            return False
        for key in obj1:
            if key not in obj2:
                return False
            if not compare_json(obj1[key], obj2[key]):
                return False
        return True

    if isinstance(obj1, list):
        if len(obj1) != len(obj2):
            return False
        for i in range(len(obj1)):
            if not compare_json(obj1[i], obj2[i]):
                return False
        return True

    return obj1 == obj2