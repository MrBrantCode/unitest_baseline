"""
QUESTION:
Implement a function `binary_search` that takes in a sorted array of integers and a target integer, and returns the index of the target integer in the array if it exists, or -1 otherwise. The function should have a time complexity of O(log n), where n is the number of elements in the array.
"""

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1