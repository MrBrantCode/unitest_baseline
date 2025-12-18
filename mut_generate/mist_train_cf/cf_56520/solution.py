"""
QUESTION:
Write a function named `find_max` that takes an array of integers as input and returns the maximum value in the array. The function should only use bitwise operations for comparisons and not utilize any built-in functions like max().
"""

def find_max(arr):
    max_val = arr[0]

    for num in arr:
        if (max_val - num) >> 31 & 1:
            max_val = num
            
    return max_val