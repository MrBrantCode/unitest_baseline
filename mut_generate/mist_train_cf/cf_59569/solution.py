"""
QUESTION:
Write a function `get_size_of_tuple(obj)` to calculate the total size in bytes of a given tuple and its nested data structures (including lists, sets, and dictionaries), excluding the size of any string, integer, or float elements they may contain. The function should handle cases where the tuple or its nested structures reference each other. The function should return the total size in bytes, which can be used to compare the sizes of different objects but may not be precisely accurate.
"""

import sys

def get_size_of_tuple(obj, seen=None):
    size = sys.getsizeof(obj)
    
    if seen is None:
        seen = set()

    obj_id = id(obj)
    
    # To handle recursion (objects referring to each other)
    if obj_id in seen:
        return 0

    # Add the size of the current object to the set of seen objects
    seen.add(obj_id)

    if isinstance(obj, tuple):
        size += sum(get_size_of_tuple(item, seen) for item in obj)
    elif isinstance(obj, dict):
        size += sum(get_size_of_tuple(v, seen) for v in obj.values())
        size += sum(get_size_of_tuple(k, seen) for k in obj.keys())
    elif isinstance(obj, list) or isinstance(obj, set):
        size += sum(get_size_of_tuple(item, seen) for item in obj)

    # Subtract size of string, int, and float value
    if isinstance(obj, (str, int, float)):
        size -= sys.getsizeof(obj)
    
    return size