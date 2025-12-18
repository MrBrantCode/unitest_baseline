"""
QUESTION:
Write a function named `linear_search_sorted` that takes two parameters: `arr` (a sorted list of elements) and `target` (the element to be searched). The function should return the index of the `target` element in the `arr` if found, and -1 otherwise. Assume that the `arr` is sorted in ascending order and all elements are unique.
"""

def linear_search_sorted(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
        if arr[i] > target:
            return -1
    return -1