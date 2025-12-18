"""
QUESTION:
Write a function named `find_max` that takes an array of integers as input and returns the maximum value in the array without using any built-in functions such as max() or sorted(). The array may contain positive, negative, and zero values.
"""

def find_max(arr):
    max_val = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
    return max_val