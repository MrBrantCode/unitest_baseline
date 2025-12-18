"""
QUESTION:
Implement a function called `search` that takes a sorted array and a target number as input and returns the index of the first occurrence of the target number in the array. The function must have a time complexity of O(log n), cannot use any built-in search functions or libraries, and cannot use additional space apart from a few constant variables. The array may contain duplicate elements. If the target number is not found, return -1.
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