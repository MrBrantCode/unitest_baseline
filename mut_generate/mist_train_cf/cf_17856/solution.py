"""
QUESTION:
Write a function called `remove_duplicates` that takes an array as input and returns a new array with duplicate elements removed while preserving the original order. The input array may contain integers, strings, or a combination of both. The function should handle large input arrays efficiently with a time complexity of O(n) or less.
"""

def remove_duplicates(arr):
    unique = []
    seen = set()
    for item in arr:
        if item not in seen:
            unique.append(item)
            seen.add(item)
    return unique