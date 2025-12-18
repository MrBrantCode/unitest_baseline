"""
QUESTION:
Create a function `max_increasing_length(arr)` that finds the maximum length of a strictly increasing subarray in the given list of integers. The function should return the length of the longest subarray where each element is strictly greater than the previous one. If the input list is empty, return -1. If the list contains only one element, return 0.
"""

def max_increasing_length(arr):
    if len(arr) == 0:
        return -1
    elif len(arr) == 1:
        return 0
    
    max_length = 1
    current_length = 1
    
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]: # corrected the condition to strictly greater
            current_length += 1
        else:
            max_length = max(max_length, current_length)
            current_length = 1
    
    return max(max_length, current_length)