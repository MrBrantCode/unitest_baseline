"""
QUESTION:
Implement a recursive binary search function `binary_search` that finds the index of a given number in a sorted array. The function should have a time complexity of O(log n) and use constant extra space. The function should take a sorted array, the left index, the right index, and the target number as arguments and return the index of the target number if found, or -1 if not found.
"""

def binary_search(arr, left, right, target):
    if left > right:
        return -1  # target not found

    mid = left + (right - left) // 2

    if arr[mid] == target:
        return mid  # target found at index mid

    if arr[mid] > target:
        return binary_search(arr, left, mid - 1, target)  # search in the left half

    return binary_search(arr, mid + 1, right, target)  # search in the right half