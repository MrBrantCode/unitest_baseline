"""
QUESTION:
Write a function `remove_duplicates` that takes an array of integers and strings as input, removes duplicates while preserving the order of elements, and returns the resulting array. The function should have a time complexity of O(n) or less, where n is the number of elements in the input array.
"""

def remove_duplicates(arr):
    unique = []
    seen = set()
    for item in arr:
        if item not in seen:
            unique.append(item)
            seen.add(item)
    return unique