"""
QUESTION:
Write a function `find_max(arr)` that returns the maximum element in the given array `arr`. The array contains integers and can be empty, but it is guaranteed to have at least one element if it is not empty. Do not use any built-in functions, libraries, or additional data structures. The function should optimize for both time and space complexity.
"""

def find_max(arr):
    max_element = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_element:
            max_element = arr[i]
    return max_element