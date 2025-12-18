"""
QUESTION:
Implement a recursive function `binary_search_recursive` that performs a binary search on a sorted list `arr` to find the index of a target value `target`. The function should have a time complexity of O(log n) and space complexity of O(1), and handle the case where the list contains only one item. The function should take four parameters: `arr`, `target`, `left`, and `right`, where `left` and `right` represent the current search space.
"""

def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)