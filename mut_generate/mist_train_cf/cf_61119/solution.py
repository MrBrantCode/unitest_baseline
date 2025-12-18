"""
QUESTION:
Write a function `kth_element(arr1, arr2, k)` that merges two sorted arrays `arr1` and `arr2`, sorts the merged array in ascending order, and returns the kth element (1-based index). The function should work with arrays containing elements of different data types (integers, floats, strings) and return `None` if `k` is greater than the total number of elements in the two arrays.
"""

def kth_element(arr1, arr2, k):
    total_len = len(arr1) + len(arr2)
    
    if k > total_len:
        return None

    result = arr1 + arr2
    result.sort()
    return result[k - 1]