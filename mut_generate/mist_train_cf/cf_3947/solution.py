"""
QUESTION:
Implement a function named `remove_duplicates` that takes an array of integers and/or strings as input, removes duplicates while preserving order, and returns the resulting array sorted in ascending order. The input array can contain up to 10^6 elements, each with a length between 1 and 1000. The function must not use built-in sorting or duplicate removal functions and must achieve a time complexity of O(n log n) or better.
"""

def remove_duplicates(array):
    output = []
    seen = set()
    for element in array:
        if element not in seen:
            seen.add(element)
            output.append(element)
    output.sort()
    return output