"""
QUESTION:
Implement a function called `binary_search(arr, target)` that performs a binary search on a sorted array in ascending order and returns the index of the first occurrence of the target element if it is present multiple times in the array. If the target element is not found, return the index of the nearest smaller element. The function should have a time complexity of O(log n), where n is the number of elements in the input array.
"""

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            result = mid
            right = mid - 1  # Move to the left to find the first occurrence
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    if result == -1:
        return left - 1
    else:
        return result