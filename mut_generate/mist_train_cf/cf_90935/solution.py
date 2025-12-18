"""
QUESTION:
Create a function named `compare_json` that compares two JSON objects recursively. The function should return `True` if the objects are identical, including all nested levels and data types, and `False` otherwise. The input objects can contain any valid JSON data types, including objects, arrays, strings, numbers, booleans, and null. The function should not modify the input objects.
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