"""
QUESTION:
Write a function called `delete_element(arr, target)` that takes a list `arr` and a target element `target` as input, removes all occurrences of `target` from `arr`, and returns `True` if `target` is found in `arr` and `False` otherwise. The function should only iterate over `arr` once, have a time complexity of O(n), and use constant space complexity.
"""

def delete_element(arr, target):
    found = False
    i = 0
    while i < len(arr):
        if arr[i] == target:
            arr.pop(i)
            found = True
        else:
            i += 1
    return found