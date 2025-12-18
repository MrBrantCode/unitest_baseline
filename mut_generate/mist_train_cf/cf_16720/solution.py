"""
QUESTION:
Write a function `concat_arrays(arr1, arr2)` that takes two arrays as input, concatenates them, removes any duplicate elements, and removes any negative numbers from the resulting array. The function should return the resulting array.
"""

def concat_arrays(arr1, arr2):
    # concatenate the two arrays
    result = arr1 + arr2
    
    # remove duplicate elements
    result = list(set(result))
    
    # remove negative numbers
    result = [x for x in result if x >= 0]
    
    return result