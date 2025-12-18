"""
QUESTION:
Write a function `findMax` that takes an array of integers as input and returns the maximum integer in the array.
"""

def findMax(arr):
    max_val = arr[0]
    for num in arr[1:]:
        if num > max_val:
            max_val = num
    return max_val