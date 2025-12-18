"""
QUESTION:
Write a function `linear_search(arr, target)` that searches for the first occurrence of the target element in the given array and returns its index. If the target element is not found, return -1. The function should terminate as soon as it finds the first occurrence of the target element. What is the Big O notation of this function?
"""

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1