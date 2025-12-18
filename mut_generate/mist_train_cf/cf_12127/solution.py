"""
QUESTION:
Write a function `mergeArrays(ar1, ar2)` to merge two sorted arrays `ar1` and `ar2` into a single sorted array. The function should be recursive and not use any built-in sorting functions or additional data structures. If either `ar1` or `ar2` is empty, the function should return the other array as the merged result.
"""

def mergeArrays(ar1, ar2):
    # Check if either ar1 or ar2 is empty
    if len(ar1) == 0:
        return ar2
    if len(ar2) == 0:
        return ar1

    # Compare and merge the first elements of ar1 and ar2
    if ar1[0] <= ar2[0]:
        return [ar1[0]] + mergeArrays(ar1[1:], ar2)
    else:
        return [ar2[0]] + mergeArrays(ar1, ar2[1:])