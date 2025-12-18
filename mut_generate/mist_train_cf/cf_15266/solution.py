"""
QUESTION:
Write a function `binary_search_first_occurrence` that performs a binary search on a sorted array to find the first occurrence of a target element. The function should return the index of the first occurrence if the target element is present, and -1 otherwise. The function should have a time complexity of O(log n) and a space complexity of O(1). The input array is assumed to contain duplicate elements.
"""

def binary_search_first_occurrence(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            if mid == 0 or arr[mid - 1] != target:
                return mid
            else:
                high = mid - 1
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1