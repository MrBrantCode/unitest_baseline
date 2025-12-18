"""
QUESTION:
Implement a function called `binary_search` that takes two parameters: a sorted array of elements in ascending order (which may contain duplicates) and a target element. The function should return the index of the first occurrence of the target element if it exists in the array, or a specific value to indicate that the target element is not found. The function should have a time complexity of O(log n), where n is the number of elements in the input array.
"""

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            result = mid
            right = mid - 1  # Move to the left to find the first occurrence
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result