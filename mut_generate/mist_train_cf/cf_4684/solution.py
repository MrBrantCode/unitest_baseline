"""
QUESTION:
Write a function `merge_sorted_subarrays(ar1, ar2)` that takes two subarrays `ar1` and `ar2` as input, merges them, and returns the merged array in ascending order. The function should be implemented recursively without using any built-in sorting functions or additional data structures. Note that the input arrays may contain duplicate elements and may not be fully sorted.
"""

def merge_sorted_subarrays(ar1, ar2):
    # Check if either ar1 or ar2 is empty
    if len(ar1) == 0:
        return ar2
    if len(ar2) == 0:
        return ar1
    
    # Compare the first elements of ar1 and ar2
    if ar1[0] <= ar2[0]:
        # Append the first element of ar1 to the result array
        return [ar1[0]] + merge_sorted_subarrays(ar1[1:], ar2)
    else:
        # Append the first element of ar2 to the result array
        return [ar2[0]] + merge_sorted_subarrays(ar1, ar2[1:])