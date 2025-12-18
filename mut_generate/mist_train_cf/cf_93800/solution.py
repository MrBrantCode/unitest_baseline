"""
QUESTION:
Write a function named find_maximum that takes an array of integers as input and returns the maximum element in the array. The function should analyze its time complexity and space complexity using Big O notation.
"""

def find_maximum(arr):
    max_val = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
    return max_val