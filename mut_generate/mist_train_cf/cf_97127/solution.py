"""
QUESTION:
Write an iterative function `find_kth_smallest` that takes a sorted array `arr` of size `n` and an integer `k` as input, and returns the kth smallest element in the array. The function should have a time complexity of O(log n) and should not use any additional space.
"""

def find_kth_smallest(arr, k):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == k:
            return arr[mid]
        elif arr[mid] > k:
            right = mid - 1
        else:
            left = mid + 1

    return -1