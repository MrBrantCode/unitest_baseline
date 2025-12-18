"""
QUESTION:
Write a function `binary_search(arr, target)` that searches for the `target` element in a sorted list `arr`. The function should return the index of the `target` element if found, and -1 otherwise. The function must have a time complexity of O(log n), where n is the length of the list.
"""

def entance(arr, target):
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

    return -1