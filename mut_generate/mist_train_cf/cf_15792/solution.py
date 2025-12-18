"""
QUESTION:
Implement a function named `binary_search` that takes a sorted list of integers and a target integer as input. The function should return the index of the target integer if it exists in the list, and -1 otherwise. The function should have a time complexity of O(log n) and a space complexity of O(1).
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
    
    return -1  # Target number not found