"""
QUESTION:
Implement a function named `binary_search` that takes two parameters: a sorted list of integers `arr` and a target integer `target`. The function should return the index of the target integer in the list if found, and -1 if the target integer is not present in the list. The function should have a time complexity of O(log n) and a space complexity of O(1), where n is the number of elements in the list.
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