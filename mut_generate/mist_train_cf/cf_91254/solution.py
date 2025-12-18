"""
QUESTION:
Implement a function `find_maximum(arr)` to find the maximum number in a given array of integers without using built-in functions or methods for finding the maximum. The array can be empty or contain both positive and negative numbers. If the array is empty, the function should return `None`.
"""

def find_maximum(arr):
    if len(arr) == 0:
        return None

    max_num = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_num:
            max_num = arr[i]

    return max_num