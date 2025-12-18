"""
QUESTION:
Write a function named `linear_search_sorted` that performs a linear search on a sorted array to find the index of a given target element. The function should take two parameters, `arr` (the sorted array) and `target` (the element to be searched), and return the index of the target element if found, or -1 if not found. The function should have a time complexity of O(n), where n is the size of the array.
"""

def linear_search_sorted(arr, target):
    for i in range(len(arr)):
        if arr[i] >= target:
            if arr[i] == target:
                return i
            else:
                return -1
    return -1