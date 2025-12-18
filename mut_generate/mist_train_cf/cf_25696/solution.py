"""
QUESTION:
Design a method called `mergeArrays` that takes in two sorted arrays `arr1` and `arr2` of sizes `n` and `m` respectively, and returns a new sorted array of size `n + m`. The function should not use any built-in sorting methods.
"""

def mergeArrays(arr1, arr2):
    """
    Merge two sorted arrays into a new sorted array.

    Args:
    arr1 (list): The first sorted array.
    arr2 (list): The second sorted array.

    Returns:
    list: A new sorted array containing all elements from arr1 and arr2.
    """
    result = [0] * (len(arr1) + len(arr2))
    i, j, k = 0, 0, 0
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result[k] = arr1[i]
            i += 1
        else:
            result[k] = arr2[j]
            j += 1
        k += 1
    
    while i < len(arr1):
        result[k] = arr1[i]
        i += 1
        k += 1
    
    while j < len(arr2):
        result[k] = arr2[j]
        j += 1
        k += 1
    
    return result