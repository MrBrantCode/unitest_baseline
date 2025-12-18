"""
QUESTION:
Write a function named `is_equal` that takes two Python objects as input and returns `True` if the objects have the same values, and `False` otherwise. The objects can be of any type, including integers, floats, strings, booleans, lists, tuples, dictionaries, and sets, and can have nested structures. The order of elements in lists and tuples should not matter, the order of key-value pairs in dictionaries should not matter, and the order of elements in sets should not matter.
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