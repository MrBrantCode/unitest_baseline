"""
QUESTION:
Implement a function `linear_search(arr, target)` that performs a linear search in the given array of integers and returns a list of indices of all occurrences of the target element. If the target element is not found, return an empty list. The function should have a time complexity of O(n), where n is the size of the array, and should not use any built-in functions or libraries for searching.
"""

def linear_search(arr, target):
    indices = []
    for i in range(len(arr)):
        if arr[i] == target:
            indices.append(i)
    return indices