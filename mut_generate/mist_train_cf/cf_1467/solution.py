"""
QUESTION:
Write a function named `binary_search` that takes a sorted array `arr` and a target value `target` as input, and returns the index of the target value in the array if found, or -1 otherwise. The function should use a recursive binary search algorithm with a time complexity of O(log n), where n is the size of the input array. The function should handle arrays of size up to 10^6 efficiently, handle negative integers, and not use any built-in sorting or searching functions or additional data structures other than the input array.
"""

def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return -1