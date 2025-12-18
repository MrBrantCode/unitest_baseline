"""
QUESTION:
Write a function `first_consecutive_index` that takes a list of integers as input and returns the index of the first occurrence of an element that appears consecutively at least three times in a row. If no such element exists, return -1.
"""

def first_consecutive_index(arr):
    for i in range(len(arr) - 2):
        if arr[i] == arr[i+1] == arr[i+2]:
            return i
    return -1