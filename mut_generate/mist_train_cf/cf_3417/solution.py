"""
QUESTION:
Implement a function `binary_search(arr, target)` that performs a binary search on a sorted array `arr` to find the index of a specific element `target`. The function should have a time complexity of O(log n), where n is the size of the input data, and raise a custom `ElementNotFoundException` if the target is not found in the array. The input array is guaranteed to be sorted, and the function should return the index of the target element if found.
"""

class ElementNotFoundException(Exception):
    pass

def entrance(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    raise ElementNotFoundException("Element not found in the array.")