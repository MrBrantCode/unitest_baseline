"""
QUESTION:
Implement a function `compare_objects(obj1, obj2)` that compares two objects and returns an integer value indicating their relative order. The function should accept integers or strings as input. When comparing strings, the comparison should be case-insensitive and based on the ASCII values of the characters. The function should return 0 if the objects are equal, -1 if `obj1` is less than `obj2`, and 1 if `obj1` is greater than `obj2`. If the objects are of different types, the function should return `None`.
"""

def compare_objects(obj1, obj2):
    # Check if the objects are of different types
    if type(obj1) != type(obj2):
        return None

    # Case-insensitive comparison for strings
    if isinstance(obj1, str) and isinstance(obj2, str):
        obj1 = obj1.upper()
        obj2 = obj2.upper()

    # Compare the ASCII values of each character
    if isinstance(obj1, str):
        if obj1 < obj2:
            return -1
        elif obj1 > obj2:
            return 1
    else:
        if obj1 < obj2:
            return -1
        elif obj1 > obj2:
            return 1

    # If the loop finishes without returning, the strings are equal
    return 0