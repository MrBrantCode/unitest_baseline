"""
QUESTION:
Write a function `find_kth_smallest(A, B, k)` that takes two sorted arrays `A` and `B` of positive integers with no duplicates and an integer `k` as input, and returns the k-th smallest element in the merged array of `A` and `B`. The arrays are 0-indexed, so the k-th smallest element corresponds to the index `k - 1`.
"""

def entrance(A, B, k):
    merged_array = sorted(A + B)
    return merged_array[k - 1]