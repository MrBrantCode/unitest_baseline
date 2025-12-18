"""
QUESTION:
Implement an iterative binary search algorithm in a function named `binary_search` that searches for a target element in a sorted array. The function should have a time complexity of O(log n) and a space complexity of O(1), where n is the size of the array. If the target element is present multiple times in the array, the function should return the index of the first occurrence of the target element. The function should take two parameters: a sorted array and the target element. If the target element is not found, the function should return -1.
"""

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            # Check if it's the first occurrence of the target element
            while mid > 0 and arr[mid - 1] == target:
                mid -= 1
            return mid

        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1