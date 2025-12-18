"""
QUESTION:
Implement a function named `binary_search` that takes a sorted array `arr` and a target element `target` as input. The function should return the index of the target element if it exists in the array. If the target element is not found, it should raise a custom exception named `ElementNotFoundException`. The time complexity of the function should be O(log n), where n is the size of the input array.
"""

class ElementNotFoundException(Exception):
    pass

def binary_search(arr, target):
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