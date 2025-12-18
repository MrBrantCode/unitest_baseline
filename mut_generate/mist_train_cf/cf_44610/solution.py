"""
QUESTION:
Given an integer array, write a function named `sum_odd_length_subarrays` that calculates the sum of all subarrays with an odd length. The function should be efficient with a linear time complexity O(N) and handle arrays of length up to 10^5 with elements in the range of 1 to 100.
"""

def sum_odd_length_subarrays(arr):
    res = 0
    n = len(arr)
    for i in range(n):
        res += ((i+1)*(n-i)+1)//2*arr[i]
    return res