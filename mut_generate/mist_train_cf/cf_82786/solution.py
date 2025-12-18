"""
QUESTION:
Write a function named `get_size` that calculates the total memory footprint in bytes of a given tuple, including all nested objects. The function should recursively account for the memory occupied by objects within lists, dictionaries, and other iterable objects, and it should prevent double counting by keeping track of objects that have already been counted.
"""

import sys

def get_size(obj, seen=None):
    """Recursively find the size of object in bytes"""
    size = sys.getsizeof(obj)
    if seen is None:
        seen = set()
    obj_id = id(obj)
    if obj_id in seen:
        return 0
    seen.add(obj_id)
    if isinstance(obj, dict):
        size += sum([get_size(v, seen) for v in obj.values()])
        size += sum([get_size(k, seen) for k in obj.keys()])
    elif hasattr(obj, '__dict__'):
        size += get_size(obj.__dict__, seen)
    elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes, bytearray)):
        size += sum([get_size(i, seen) for i in obj])
    return size