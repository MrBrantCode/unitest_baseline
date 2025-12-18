"""
QUESTION:
Create a function `find_index(arr, target)` that takes an array `arr` and an integer `target` as input, and returns the index of the first occurrence of `target` in `arr`. The function should have a time complexity of O(n^2), where n is the length of `arr`, and should be able to handle arrays with duplicate values. If `target` is not found in `arr`, return -1.
"""

def find_index(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1