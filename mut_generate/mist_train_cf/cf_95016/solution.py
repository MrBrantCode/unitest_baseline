"""
QUESTION:
Implement the `binary_search` function to find the index of a target number in a sorted array using a recursive approach and constant extra space. The array is guaranteed to be in ascending order, contain distinct integers, and have a length of n. The function should take the array, the left index, the right index, and the target number as input and return the index of the target number if found, or -1 otherwise. The time complexity should be O(log n).
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