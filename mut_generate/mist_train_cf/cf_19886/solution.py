"""
QUESTION:
Implement a function named `binary_search(arr, target)` that performs a binary search on a sorted array of strings to find the index of the first occurrence of the target string. The function should have a time complexity of O(log n), where n is the number of elements in the array. The array may contain duplicate strings. If the target string is not found, the function should return -1.
"""

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        # Check if the middle element matches the target
        if arr[mid] == target:
            # Check if it's the first occurrence of the target
            if mid == 0 or arr[mid - 1] != target:
                return mid
            else:
                right = mid - 1

        # If the target is less than the middle element, search the left half
        elif arr[mid] > target:
            right = mid - 1

        # If the target is greater than the middle element, search the right half
        else:
            left = mid + 1

    return -1  # Target string not found