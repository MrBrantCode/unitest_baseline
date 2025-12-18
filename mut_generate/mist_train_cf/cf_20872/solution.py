"""
QUESTION:
Implement a function `binary_search(arr, target)` to check if an element `target` is present in a sorted array `arr` in ascending order. The function should have a time complexity of O(log n), where n is the size of the array. Do not use the built-in binary search function or any existing search algorithm. Implement the binary search algorithm from scratch.
"""

def entance(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False