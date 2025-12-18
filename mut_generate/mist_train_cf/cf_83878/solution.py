"""
QUESTION:
Implement a function `binary_search(arr, target)` that performs a binary search on a sorted array with duplicate elements to find the first occurrence of the target element. The array is guaranteed to be sorted, but may contain duplicate elements. Return the index of the first occurrence of the target element, or -1 if the target element is not found.
"""

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    result = -1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            result = mid     # Update the result to current mid.
            right = mid - 1  # Narrow the search space to left subarray.
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return result