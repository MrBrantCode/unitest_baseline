"""
QUESTION:
Implement a function `binary_search(arr, target)` that returns True if the target value exists in the given sorted list `arr` and False otherwise. The function should handle lists containing only one item and achieve a time complexity of O(log n) and a space complexity of O(1).
"""

def binary_search(arr, target):
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