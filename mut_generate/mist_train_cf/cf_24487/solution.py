"""
QUESTION:
Write a function named `is_sorted` that takes an array of integers as input and returns a boolean value indicating whether the array is sorted in ascending order or not.
"""

def is_sorted(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True