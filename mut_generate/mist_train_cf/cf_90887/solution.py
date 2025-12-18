"""
QUESTION:
Implement a function named `binary_search` that takes a sorted list `arr` and a target value `target` as input, and returns the index of the target value if it exists in the list, or -1 if it does not exist. The function should have a time complexity of O(log n), where n is the number of elements in the list.
"""

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        
        if guess == target:
            return mid
        elif guess > target:
            high = mid - 1
        else:
            low = mid + 1
    
    return -1