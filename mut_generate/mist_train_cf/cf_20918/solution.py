"""
QUESTION:
Write a function named `binary_search` that takes a sorted array `arr` and a target value `target` as input, and returns the index of the target value in the array if it exists, or -1 if it does not. Assume the array is sorted in ascending order and the target value is a single element. The function should have a time complexity of O(log n), where n is the size of the input array.
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
    
    return -1