"""
QUESTION:
Write a function named `linear_search` that performs a linear search for a target integer in a given list of integers. The function should return the index of the target element if found, and -1 if the target is not in the list. The list may contain duplicates. Implement the function with a time complexity of O(n) and a space complexity of O(1).
"""

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1