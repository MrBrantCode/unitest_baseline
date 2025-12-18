"""
QUESTION:
Design a function `kth_smallest_element` that takes an array `arr` and an integer `k` as input, and returns the kth smallest element in the array. The array may contain duplicate values. Assume that `k` is within the bounds of the array size, i.e., 1 ≤ `k` ≤ length of `arr`.
"""

def kth_smallest_element(arr, k):
    arr.sort()
    return arr[k - 1]