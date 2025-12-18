"""
QUESTION:
Write a function named `min_decreasing_length` that takes a list of integers as input and returns the minimum length of the shortest consecutive decreasing subsequence. If no decreasing subsequence is found, return -1. The function should process the input list from front to back.
"""

def min_decreasing_length(arr):
    n = len(arr)
    min_length = n+1  
    current_length = 1

    for i in range(1, n):
        if arr[i] < arr[i-1]:  
            current_length += 1
        else:  
            if current_length < min_length:
                min_length = current_length
            current_length = 1  

    if current_length < min_length:
        min_length = current_length

    return min_length if min_length <= n else -1  