"""
QUESTION:
Create a function called `binary_search` that takes a sorted list of integers and a target number as input, and returns the index of the first occurrence of the target number in the list. If the target number does not exist in the list, return -1. The function should have a time complexity of O(log n) and be able to handle duplicates in the list.
"""

def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            while mid > 0 and arr[mid-1] == target:
                mid -= 1
            return mid
        elif arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return -1