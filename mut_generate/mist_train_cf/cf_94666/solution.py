"""
QUESTION:
Write a function called `check_equal` that takes two arguments `obj1` and `obj2` and returns True if the objects are equal, and False otherwise. The objects can be of any type, including integers, floats, strings, booleans, lists, tuples, dictionaries, and sets, and can have nested structures. The order of elements in lists and tuples should not matter, the order of key-value pairs in dictionaries should not matter, and the order of elements in sets should not matter.
"""

def check_equal(obj1, obj2):
    # Check if obj1 and obj2 are dictionaries
    if isinstance(obj1, dict) and isinstance(obj2, dict):
        # Check if the keys and values match for both dictionaries
        return all(key in obj2 and check_equal(obj1[key], obj2[key]) for key in obj1) and all(key in obj1 and check_equal(obj1[key], obj2[key]) for key in obj2)
    
    # Check if obj1 and obj2 are lists or tuples
    elif isinstance(obj1, (list, tuple)) and isinstance(obj2, (list, tuple)):
        # Check if the lengths and elements match for both lists or tuples
        return len(obj1) == len(obj2) and all(check_equal(elem1, elem2) for elem1, elem2 in zip(sorted(obj1), sorted(obj2)))
    
    # Check if obj1 and obj2 are sets
    elif isinstance(obj1, set) and isinstance(obj2, set):
        # Check if the lengths and elements match for both sets
        return len(obj1) == len(obj2) and obj1 == obj2
    
    # Check if obj1 and obj2 are strings, integers, floats, or booleans
    elif isinstance(obj1, (str, int, float, bool)) and isinstance(obj2, (str, int, float, bool)):
        # Check if the values match for both objects
        return obj1 == obj2
    
    # Default case: return False
    return False