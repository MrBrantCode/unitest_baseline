"""
QUESTION:
Implement the function binary_search_recursive that performs a binary search on a sorted list arr to find the index of the target value. The function should have a time complexity of O(log n) and space complexity of O(1). It should be able to handle cases where the list contains only one item and should return -1 if the target value is not found in the list.
"""

def entrance(arr, target, left, right):
    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return entrance(arr, target, mid + 1, right)
    else:
        return entrance(arr, target, left, mid - 1)