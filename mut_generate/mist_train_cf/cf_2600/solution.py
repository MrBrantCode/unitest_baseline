"""
QUESTION:
Write a function `binary_search(arr, target)` that finds the index of the target element in a sorted array `arr` in descending order, using binary search. The function should return the index of the target element if found, and -1 otherwise. Assume the input array is sorted in descending order. The function should have a time complexity of O(log n), where n is the number of elements in the input array.
"""

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            high = mid - 1
        else:
            low = mid + 1

    return -1