"""
QUESTION:
Write a function `arrange_checker` that takes a vector of unique integers as input and returns the index of the earliest element that is greater than the subsequent element. If no such element exists, the function should return -1.
"""

def arrange_checker(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            return i
    return -1