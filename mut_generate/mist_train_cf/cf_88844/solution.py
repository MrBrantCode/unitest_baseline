"""
QUESTION:
Write a function `first_consecutive_index` that takes an array as input and returns the index of the first occurrence of an element that occurs consecutively at least four times in a row. If no such element is found, return -1. The function should be able to handle arrays of any length, but it should only consider consecutive elements, not the entire array.
"""

def first_consecutive_index(arr):
    for i in range(len(arr) - 3):
        if arr[i] == arr[i+1] == arr[i+2] == arr[i+3]:
            return i
    return -1