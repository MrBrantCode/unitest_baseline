"""
QUESTION:
Implement a function named `binary_search` that takes a sorted list of integers `arr` and a target integer `target` as input, and returns the index of the target in the list if found, or -1 otherwise. The function should use a while loop and have a time complexity of O(log n) to efficiently handle large lists of up to 1 million integers.
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