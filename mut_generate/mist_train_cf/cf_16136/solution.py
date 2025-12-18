"""
QUESTION:
Implement a function called `binary_search` that performs a binary search on a given sorted array to find the index of the last occurrence of a target element. The array may contain duplicate elements and will always be sorted in ascending order. The function should return the index of the last occurrence of the target element if it is present in the array; otherwise, it should return -1.
"""

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            result = mid
            left = mid + 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result