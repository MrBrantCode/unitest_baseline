"""
QUESTION:
Create a function `find_consecutive_pairs` that takes an array `arr` and an integer `value` as input, and returns the indices of the first occurrence of two consecutive elements in `arr` that are equal to `value`. If no such pair is found, return `None`. The input array `arr` will have at least three elements.
"""

def find_consecutive_pairs(arr, value):
    for i in range(len(arr)-1):
        if arr[i] == value and arr[i+1] == value:
            return [i, i+1]
    return None