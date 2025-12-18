"""
QUESTION:
Write a function `find_maximum` that takes an array of integers as input and returns the maximum value and its index. The function should have a time complexity of O(n) and use constant space, where n is the length of the array.
"""

def find_maximum(arr):
    max_val = arr[0]
    max_index = 0
    
    for i in range(1, len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
            max_index = i
    
    return max_val, max_index