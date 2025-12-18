"""
QUESTION:
Implement the `binary_search` function to find a target value in a sorted list of integers. The function should return `True` if the target value is found and `False` otherwise. It must handle lists containing only one item and have a time complexity of O(log n) and a space complexity of O(1).
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