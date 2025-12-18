"""
QUESTION:
Write a function `maxTurbulenceSize` that determines the length of the largest turbulent subarray within a given integer array. A subarray is considered turbulent if the comparison sign alternates between each successive pair of elements. The function should take one integer array `arr` as input and return an integer representing the length of the largest turbulent subarray. The length of `arr` is between 1 and 4 * 10^4, and each element in `arr` is between 0 and 10^9.
"""

def maxTurbulenceSize(arr):
    n = len(arr)
    res, inc, dec = 1, 1, 1
    for i in range(1, n):
        if arr[i] > arr[i-1]:
            inc, dec = dec + 1, 1
        elif arr[i] < arr[i-1]:
            inc, dec = 1, inc + 1
        else:
            inc, dec = 1, 1
        res = max(res, inc, dec)
    return res