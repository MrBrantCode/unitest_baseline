"""
QUESTION:
Write a function `find_kth_smallest(arr, k)` that returns the kth smallest element in a sorted array `arr` of size `n` using an iterative approach with a time complexity of O(log n) and without using any additional space. The function should return -1 if the kth smallest element does not exist.
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