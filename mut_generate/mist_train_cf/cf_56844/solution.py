"""
QUESTION:
Write a function `getMedian(arr1, arr2)` that calculates the median of two sorted arrays of identical length. The function should return the median value as a float if the total length of the arrays is even, and as a single value if the total length is odd.
"""

def getMedian(arr1, arr2):
    mergedArray = sorted(arr1 + arr2)
    n = len(mergedArray)
    if n % 2 == 0:
        return (mergedArray[n//2] + mergedArray[n//2 - 1]) / 2
    else:
        return mergedArray[n//2]