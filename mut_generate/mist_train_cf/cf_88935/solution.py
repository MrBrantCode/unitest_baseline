"""
QUESTION:
Implement a function named `find_max_min` that takes an array of integers as input and returns the minimum value, its index, the maximum value, and its index. The function should have a time complexity of O(n) and a space complexity of O(1). If the input array is empty, the function should return an error message.
"""

def find_max_min(arr):
    if len(arr) == 0:
        return "Error: Empty array"
    
    min_val = arr[0]
    max_val = arr[0]
    min_idx = 0
    max_idx = 0
    
    for i in range(1, len(arr)):
        if arr[i] < min_val:
            min_val = arr[i]
            min_idx = i
        elif arr[i] > max_val:
            max_val = arr[i]
            max_idx = i
            
    return (min_val, min_idx, max_val, max_idx)