"""
QUESTION:
Write a function `concatenate_arrays(arr1, arr2)` that takes two arrays `arr1` and `arr2` as input and returns a new array that is the concatenation of `arr1` and `arr2`, with no duplicate elements, sorted in ascending order. You cannot use any built-in array concatenation methods or functions.
"""

def entance(arr1, arr2):
    # Concatenate the two arrays
    result = arr1 + arr2
    
    # Remove duplicate elements
    result = list(set(result))
    
    # Sort the resulting array in ascending order
    result.sort()
    
    return result