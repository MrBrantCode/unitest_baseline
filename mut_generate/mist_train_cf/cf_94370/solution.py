"""
QUESTION:
Write a function named `concat_arrays` that takes two lists `arr1` and `arr2` as input and returns a new list containing all unique non-negative elements from both lists.
"""

def concat_arrays(arr1, arr2):
    # concatenate the two arrays
    result = arr1 + arr2
    
    # remove duplicate elements and negative numbers
    result = list(set([x for x in result if x >= 0]))
    
    return result