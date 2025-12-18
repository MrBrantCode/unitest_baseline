"""
QUESTION:
Write a function called `get_size_of_object` that calculates the total size in bytes of a given tuple, considering nested tuples and excluding the size of any string, integer, float, or boolean elements. The function should handle circular references and recursive data structures, but does not need to handle user-defined types, multi-threading scenarios, or overridden Python magic methods. The function should not enter an infinite loop in cases of circular references and should correctly compute the size of the data structure, counting each distinct object only once.
"""

import sys

def get_size_of_object(obj, seen = None):
    if seen is None:
        seen = set()
    size = sys.getsizeof(obj)
    if id(obj) in seen:
        return 0
    seen.add(id(obj))
    if isinstance(obj, dict):
        size += sum([get_size_of_object(v, seen) for v in obj.values()])
        size += sum([get_size_of_object(k, seen) for k in obj.keys()])
    elif hasattr(obj, '__dict__'):
        size += get_size_of_object(obj.__dict__, seen)
    elif hasattr(obj, '__iter__') and not isinstance(obj, (str, bytes, bytearray)):
        size += sum([get_size_of_object(i, seen) for i in obj])
    return size