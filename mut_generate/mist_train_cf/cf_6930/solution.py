"""
QUESTION:
Implement a recursive binary search algorithm in a function named `binary_search` that finds the position of the first occurrence of a target element in a sorted array. The array can contain duplicate elements and must be sorted in ascending order. If the target element is not found, return -1. The function should have a time complexity of O(log n) and a space complexity of O(log n), where n is the size of the input array.
"""

def binary_search(arr, target, low, high):
    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:
        if mid == 0 or arr[mid-1] != target:
            return mid
        else:
            return binary_search(arr, target, low, mid-1)
    elif arr[mid] < target:
        return binary_search(arr, target, mid+1, high)
    else:
        return binary_search(arr, target, low, mid-1)