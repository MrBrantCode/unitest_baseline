"""
QUESTION:
Write a function `is_equal(obj1, obj2)` that checks if two Python objects `obj1` and `obj2` have the same values. The objects can be of any type, including nested structures like lists, dictionaries, and sets. The function should return `True` if the objects are equal, and `False` otherwise. The equality check should be order-independent for lists, tuples, dictionaries, and sets.
"""

def is_equal(obj1, obj2):
    if type(obj1) != type(obj2):
        return False
    if isinstance(obj1, (int, float, str, bool)):
        return obj1 == obj2
    if isinstance(obj1, list) or isinstance(obj1, tuple):
        if len(obj1) != len(obj2):
            return False
        return sorted(obj1) == sorted(obj2)
    if isinstance(obj1, dict):
        if len(obj1) != len(obj2):
            return False
        for key in obj1:
            if key not in obj2 or not is_equal(obj1[key], obj2[key]):
                return False
        return True
    if isinstance(obj1, set):
        return set(obj1) == set(obj2)
    return False