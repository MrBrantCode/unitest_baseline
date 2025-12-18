"""
QUESTION:
Write a function `check_equal` that checks if two Python objects have the same values. The objects can be of any type, including integers, floats, strings, booleans, lists, tuples, dictionaries, and sets. They can also have nested structures. The order of elements in lists, tuples, and sets, as well as the order of key-value pairs in dictionaries, should not matter.

The function should return True if the objects are equal and False otherwise.
"""

def check_equal(obj1, obj2):
    # Check if obj1 and obj2 are dictionaries
    if isinstance(obj1, dict) and isinstance(obj2, dict):
        # Check if the keys and values match for both dictionaries
        return all(key in obj2 and check_equal(obj1[key], obj2[key]) for key in obj1) and all(key in obj1 and check_equal(obj1[key], obj2[key]) for key in obj2)
    
    # Check if obj1 and obj2 are lists or tuples
    elif isinstance(obj1, (list, tuple)) and isinstance(obj2, (list, tuple)):
        # Check if the lengths and elements match for both lists or tuples
        return len(obj1) == len(obj2) and all(check_equal(elem1, elem2) for elem1, elem2 in zip(obj1, obj2))
    
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