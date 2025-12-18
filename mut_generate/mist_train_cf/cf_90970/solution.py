"""
QUESTION:
Write a function `search_target` that takes an array and a target as input, and returns the index of the first occurrence of the target in the array. If the target is not found, return -1. The array may contain duplicate elements.
"""

def search_target(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1