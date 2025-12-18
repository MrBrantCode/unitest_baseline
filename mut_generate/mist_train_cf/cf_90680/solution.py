"""
QUESTION:
Write a function `find_index(arr, item)` that finds the index of a given item in an array. If the item appears multiple times in the array, return the index of the first occurrence. If the item is not found in the array, return -1.
"""

def find_index(arr, item):
    for i in range(len(arr)):
        if arr[i] == item:
            return i
    return -1  # If item is not found