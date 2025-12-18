"""
QUESTION:
Write a function `merge_unique_arrays(array1, array2)` that merges two input arrays, removes duplicate values, and returns a new sorted array. The function should handle arrays with elements of different types. The sorting order should prioritize elements based on their types, with all non-integer values coming after integers, and then sorted alphabetically for strings and numerically for integers.
"""

def merge_unique_arrays(array1, array2):
    merged_array = list(set(array1 + array2))
    merged_array.sort(key=lambda x: (str(type(x)), x))
    return merged_array