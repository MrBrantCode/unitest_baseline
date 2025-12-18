"""
QUESTION:
Implement a function named `binary_search` that takes in two parameters: a sorted array `arr` and a target number `target`. The function should return the index of the target number in the array if found, and -1 otherwise. The time complexity of the function should be O(log n), where n is the number of elements in the array.
"""

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Return -1 if target is not found