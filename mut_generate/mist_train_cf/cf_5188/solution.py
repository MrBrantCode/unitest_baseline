"""
QUESTION:
Implement a function called `binary_search` that takes in a sorted array `arr` of strings and a target string `target`, and returns the index of the first occurrence of the target string in the array. If the target string is not found, return -1. The array can contain duplicate strings and can be up to 10 million elements in size. The function should have a time complexity of O(log n), where n is the number of elements in the array.
"""

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            if mid == 0 or arr[mid - 1] != target:
                return mid
            else:
                high = mid - 1

    return -1