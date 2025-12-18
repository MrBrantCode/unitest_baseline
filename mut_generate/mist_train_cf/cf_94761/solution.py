"""
QUESTION:
Create a function `search(arr, target)` that searches for a given number `target` in a sorted array `arr` and returns the index of the first occurrence of the number. If the number does not exist in the array, return -1. The function should have a time complexity of O(log n), where n is the length of the array, and should be able to handle arrays with duplicate elements and a maximum length of 10^7.
"""

def search(arr, target):
    left = 0
    right = len(arr) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result