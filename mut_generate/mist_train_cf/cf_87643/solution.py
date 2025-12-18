"""
QUESTION:
Write a function `linear_search_reverse(arr, target)` that performs a linear search in an array starting from the end and returns the index of the last occurrence of the target number. If the target number is not found, return -1. The function should have a time complexity of O(n), where n is the length of the array.
"""

def linear_search_reverse(arr, target):
    index = -1
    for i in range(len(arr)-1, -1, -1):
        if arr[i] == target:
            index = i
            break
    return index