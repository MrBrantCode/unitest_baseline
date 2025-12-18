"""
QUESTION:
Design a function `find_kth_largest` that takes a list of integers `arr` and an integer `k` as input. The function should return the kth largest number in the list. Assume that k is within the bounds of the list length.
"""

def find_kth_largest(arr, k):
    arr.sort(reverse=True)
    return arr[k-1]