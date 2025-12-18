"""
QUESTION:
Write a function `num_of_subarrays(arr)` that determines the total number of unique subarrays in the given array. The array can contain up to 10^3 elements and may have repeated elements. The function should return the total count of unique subarrays.
"""

from math import comb

def num_of_subarrays(arr):
    n = len(arr)
    return sum(comb(n, r) for r in range(1, n+1))