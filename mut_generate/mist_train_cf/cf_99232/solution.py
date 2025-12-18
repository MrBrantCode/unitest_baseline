"""
QUESTION:
Create a function called `remove_duplicates` that takes an array of integers as input, removes duplicate elements while preserving the order of the remaining elements, and returns the resulting array. The function should be optimized for both time and space complexity to handle potentially large arrays.
"""

def remove_duplicates(arr):
    seen = set()
    result = []
    for num in arr:
        if num not in seen:
            result.append(num)
            seen.add(num)
    return result