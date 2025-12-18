"""
QUESTION:
Write a function `remove_duplicates(array)` that removes duplicates from the given array while preserving the order of the elements. The array may contain integers, strings, or a combination of both. The function should handle large input arrays efficiently and have a time complexity of O(n) or less.
"""

def remove_duplicates(array):
    seen = set()       # Set to keep track of unique elements
    result = []        # List to store elements in order

    for element in array:
        if element not in seen:
            seen.add(element)
            result.append(element)

    return result