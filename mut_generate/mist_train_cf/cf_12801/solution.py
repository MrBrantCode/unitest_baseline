"""
QUESTION:
Write a function `find_max_index` that takes an array of positive integers as input and returns the index of the first occurrence of the maximum value. The function should return the lowest index in case of multiple occurrences of the maximum value. The input array is guaranteed to contain at least one element.
"""

def find_max_index(arr):
    max_val = max(arr)
    for i in range(len(arr)):
        if arr[i] == max_val:
            return i