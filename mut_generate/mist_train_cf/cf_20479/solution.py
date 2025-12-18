"""
QUESTION:
Create a function called `merge_objects` that takes two parameters, `a` and `b`, and returns a new object containing all keys from both `a` and `b`. If there are duplicate keys, the value from `b` should overwrite the value from `a`. The function should only include keys that contain alphabetic characters (A-Z, a-z) and exclude keys with non-alphabetic characters. The function should also handle nested objects within `a` and `b` and merge them accordingly. The resulting object should be sorted in ascending order based on the keys.
"""

def merge_objects(a, b):
    merged = {}

    # Merge keys from the first object
    for key in a:
        if key.isalpha():
            merged[key] = a[key]

    # Merge keys from the second object
    for key in b:
        if key.isalpha():
            merged[key] = b[key]

    # Merge nested objects
    for key in a:
        if isinstance(a[key], dict) and isinstance(b.get(key), dict):
            merged[key] = merge_objects(a[key], b[key])

    for key in b:
        if key not in a and isinstance(b[key], dict):
            merged[key] = merge_objects({}, b[key])

    # Sort the merged object by keys
    sorted_merged = {}
    for key in sorted(merged):
        sorted_merged[key] = merged[key]

    return sorted_merged