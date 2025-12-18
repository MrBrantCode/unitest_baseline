"""
QUESTION:
Write a function `find_consecutive_index(arr)` that takes a list of elements as input and returns the index of the first occurrence of an element that appears consecutively at least twice in a row. If no such element exists, return -1. The function should iterate through the array only once.
"""

def find_consecutive_index(arr):
    prev = None
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            return i
    return -1