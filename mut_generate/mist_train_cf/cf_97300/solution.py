"""
QUESTION:
Write a function named `linear_search` that performs a linear search on an array of integers. The function should take two parameters: `arr` (the array of integers) and `target` (the target element to be searched). It should return a list of indices of all occurrences of the target element in the array. If the target element is not found, it should return an empty list. The function should have a time complexity of O(n), where n is the size of the array, and it should not use any built-in functions or libraries for searching.
"""

def linear_search(arr, target):
    indices = []
    for i in range(len(arr)):
        if arr[i] == target:
            indices.append(i)
    return indices