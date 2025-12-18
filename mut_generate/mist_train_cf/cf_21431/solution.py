"""
QUESTION:
Implement the `linear_search` function, which takes a list of integers `arr` and a target integer `target` as input. The function should return the index of the first occurrence of `target` in `arr` if found, or -1 if `target` is not found. The function should have a time complexity of O(n), where n is the number of elements in the list, and a space complexity of O(1).
"""

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1