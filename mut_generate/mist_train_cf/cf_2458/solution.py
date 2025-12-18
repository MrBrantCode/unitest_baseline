"""
QUESTION:
Write a function named `check_objects_equal` that checks if two Python objects have the same values. The function should work with objects of any type, including integers, floats, strings, booleans, lists, tuples, dictionaries, and sets, and should handle nested structures. The function should consider the order of key-value pairs in dictionaries and the order of elements in sets, but not in lists and tuples. It should also return True if the objects are equal in value but have different data types.
"""

def check_objects_equal(obj1, obj2):
    # Check if the objects have the same type
    if type(obj1) != type(obj2):
        return False
    
    # If the objects are dictionaries, compare their key-value pairs
    if isinstance(obj1, dict):
        if len(obj1) != len(obj2):
            return False
        for key in obj1:
            if key not in obj2 or not check_objects_equal(obj1[key], obj2[key]):
                return False
        return True
    
    # If the objects are sets, compare their elements
    if isinstance(obj1, set):
        if len(obj1) != len(obj2):
            return False
        return obj1 == obj2
    
    # If the objects are lists or tuples, compare their elements regardless of order
    if isinstance(obj1, (list, tuple)):
        if len(obj1) != len(obj2):
            return False
        return set(obj1) == set(obj2)
    
    # If the objects are not dictionaries, sets, lists, or tuples, compare their values directly
    return obj1 == obj2