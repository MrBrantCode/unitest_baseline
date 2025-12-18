"""
QUESTION:
Implement a function `search(arr, target)` that searches for a target number in a sorted array `arr` and returns the index of its first occurrence. The function should have a time complexity of O(log n) and should not use any built-in search functions or libraries, or additional space apart from a few constant variables.
"""

def search(arr, target):
    left = 0
    right = len(arr) - 1
    result = -1

    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            result = mid
            right = mid - 1  # Search for first occurrence in the left half
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result