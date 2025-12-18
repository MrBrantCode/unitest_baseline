"""
QUESTION:
Create a function named `tuple_memory_usage` that calculates the total memory usage in bytes of a given tuple, including the memory consumed by the tuple object itself and its contents. The function should be able to handle nested data structures and avoid counting shared references multiple times.
"""

import sys

def tuple_memory_usage(t, seen=None):
    """Recursively finds size of objects"""
    size = sys.getsizeof(t)
    if seen is None:
        seen = set()
    obj_id = id(t)
    if obj_id in seen:
        return 0
    # Mark as seen
    seen.add(obj_id)
    if isinstance(t, dict):
        size += sum([tuple_memory_usage(v, seen) for v in t.values()])
        size += sum([tuple_memory_usage(k, seen) for k in t.keys()])
    elif hasattr(t, '__dict__'):
        size += tuple_memory_usage(t.__dict__, seen)
    elif hasattr(t, '__iter__') and not isinstance(t, (str, bytes, bytearray)):
        size += sum([tuple_memory_usage(i, seen) for i in t])
    return size