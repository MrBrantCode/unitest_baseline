"""
QUESTION:
Implement a function `binary_search(arr, target)` that uses the binary search algorithm to find the index of the first occurrence of a target element in a sorted array. The input array `arr` is sorted and may contain duplicate elements, and the `target` is the element to be searched. The function should return the index of the first occurrence of the target element if found, and -1 otherwise. The input array is guaranteed to be non-empty.
"""

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    result = -1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            result = mid
            right = mid - 1  # move left to find the first occurrence
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result