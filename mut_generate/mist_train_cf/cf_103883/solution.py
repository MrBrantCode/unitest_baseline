"""
QUESTION:
Create a function `find_index` that takes an array of integers `arr` and a target integer `target` as input, and returns the index of the `target` in the `arr`. The function must have a time complexity of O(n^2), where n is the length of `arr`. If the `target` is not found in `arr`, the function should return -1.
"""

def find_index(arr, target):
    n = len(arr)
    for i in range(n):
        if arr[i] == target:
            return i
    return -1