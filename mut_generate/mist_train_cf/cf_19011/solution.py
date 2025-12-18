"""
QUESTION:
Implement a recursive function `search_recursive` that finds the index of the first occurrence of a target element in an unsorted array that may contain duplicate elements. The function should return -1 if the target element is not found.
"""

def search_recursive(arr, target, start=0):
    if start == len(arr):
        return -1

    if arr[start] == target:
        return start

    return search_recursive(arr, target, start+1)