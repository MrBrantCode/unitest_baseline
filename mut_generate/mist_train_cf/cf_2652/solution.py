"""
QUESTION:
Create a function named `binary_search` that takes a sorted array `arr` and a target number `target` as input, and returns the index of the first occurrence of the target number in the array if it exists, or -1 if it does not. The function should have a time complexity of O(log n), where n is the length of the array, and it should be able to handle duplicate elements by returning the index of the leftmost occurrence of the number. The function should use an iterative approach and be able to handle large input arrays with a maximum length of 10^9.
"""

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    result = -1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            result = mid
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result