"""
QUESTION:
Write a function `merge_sorted_subarrays` that merges two sorted subarrays `ar1` and `ar2` into a single sorted array without using any built-in sorting functions or additional data structures. The function should handle arrays with duplicate elements and partially sorted arrays. The function should take two lists of integers as input and return the merged list. The function must be implemented recursively.
"""

def merge_sorted_subarrays(ar1, ar2):
    if len(ar1) == 0:
        return ar2
    if len(ar2) == 0:
        return ar1

    result = []
    
    if ar1[0] <= ar2[0]:
        result.append(ar1[0])
        result += merge_sorted_subarrays(ar1[1:], ar2)
    else:
        result.append(ar2[0])
        result += merge_sorted_subarrays(ar1, ar2[1:])
    
    return result