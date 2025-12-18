"""
QUESTION:
Write a function `remove_duplicates` that removes all duplicate elements from a multi-dimensional array of arbitrary depth. The function should use recursion to handle nested arrays and ensure that all duplicate elements are removed, regardless of their position in the array. The input array is not guaranteed to be symmetric, and the function should modify the original array in-place. The function should return the modified array.
"""

def remove_duplicates(arr, seen=None):
    if seen is None:
        seen = set()

    i = 0
    while i < len(arr):
        if isinstance(arr[i], list):  
            remove_duplicates(arr[i], seen) 
        elif arr[i] in seen:  
            del arr[i]
            i -= 1  
        else:
            seen.add(arr[i])  
        i += 1

    return arr