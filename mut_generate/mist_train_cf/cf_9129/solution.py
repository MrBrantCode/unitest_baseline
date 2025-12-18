"""
QUESTION:
Implement a function `binary_search(array, target)` that uses binary search to find the index of the smallest element in the sorted array `array` that is greater than the `target` value. If no such element exists, return -1. The array is sorted in ascending order. The function should have a time complexity of O(log n), where n is the number of elements in the array.
"""

def binary_search(array, target):
    left = 0
    right = len(array) - 1
    result_index = -1

    while left <= right:
        mid = (left + right) // 2

        if array[mid] > target:
            result_index = mid
            right = mid - 1
        else:
            left = mid + 1

    return result_index