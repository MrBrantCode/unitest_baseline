"""
QUESTION:
Write a Python function named `find_float` that finds and returns the index of the first occurrence of a floating point number in a provided sequence. The sequence may contain nested sequences like lists or tuples, and the function should handle these cases. If no floating point number is present in the sequence, the function should return `None`.
"""

def find_float(sequence, idx=0):
    for i, item in enumerate(sequence):
        if isinstance(item, float):
            return idx + i
        elif isinstance(item, (list, tuple)):
            result = find_float(item)
            if result is not None:
                return idx + i if idx > 0 else result
    return None