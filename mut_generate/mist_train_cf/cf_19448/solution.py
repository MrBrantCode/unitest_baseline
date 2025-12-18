"""
QUESTION:
Write a function named `findSmallest` that takes a rotated sorted array `arr` and its bounds `left` and `right` as input. The function should return the index of the smallest element in the array. The array is rotated sorted, meaning it is a sorted array that has been rotated an unknown number of times. The function should use binary search to find the smallest element efficiently. If the smallest element is not found, the function should return -1. The array bounds are 0-indexed, and the array is guaranteed to be non-empty.
"""

def findSmallest(arr, left, right):
    if right >= left:
        mid = left + (right - left) // 2
        if (mid == 0 or arr[mid] < arr[mid - 1]) and (mid == len(arr) - 1 or arr[mid] < arr[mid + 1]):
            return mid
        elif arr[mid] < arr[right]:
            return findSmallest(arr, left, mid - 1)
        else:
            return findSmallest(arr, mid + 1, right)
    return -1