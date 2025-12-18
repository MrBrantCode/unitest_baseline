"""
QUESTION:
Create a function named `linear_search` that takes two parameters: an array `arr` and a target value. This function should perform a linear search on the array to find the target value and return its index if found, or -1 if not found. The function should be able to handle arrays of varying lengths and elements.
"""

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Element found, return index
    return -1  # Element not found, return -1