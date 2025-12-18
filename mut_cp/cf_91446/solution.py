"""
ORIGINAL QUESTION:
Write a recursive function named `deep_copy` that creates a deep copy of a nested object without using any built-in methods or libraries for copying. The function should handle objects, arrays, strings, numbers, booleans, and null values.
"""

def deep_copy(obj):
    if isinstance(obj, (str, int, float, bool, type(None))):
        return obj

    if isinstance(obj, dict):
        copy = {}
        for key, value in obj.items():
            copy[key] = deep_copy(value)
        return copy

    if isinstance(obj, (list, tuple)):
        copy = []
        for element in obj:
            copy.append(deep_copy(element))
        if isinstance(obj, tuple):
            return tuple(copy)
        return copy

    return None