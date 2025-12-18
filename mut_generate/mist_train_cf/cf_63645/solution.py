"""
QUESTION:
Create a function `remove_duplicates` that takes an iterable as input and returns another iterable without duplicates, preserving the original order of elements. The function should work with any iterable object, handle case-sensitive string inputs, and check for duplicates in embedded lists. The time complexity of the function should be better than O(n^2), where n is the length of the input iterable.
"""

def remove_duplicates(iterable):
    seen = set()
    result = []
    for item in iterable:
        # For string inputs
        if isinstance(item, str) and item not in seen:
            seen.add(item)
            result.append(item)
        # For embedded list inputs
        elif isinstance(item, list) and tuple(item) not in seen:
            seen.add(tuple(item))
            result.append(item)
        # For other iterable inputs
        elif isinstance(item, (int, float)) and item not in seen:
            seen.add(item)
            result.append(item)
    return result