"""
QUESTION:
Write a function `check_target_number_exists` that takes an array of numbers `arr` and a target number `target` as input. If `target` is negative, return `False`. Otherwise, return `True` and the index of the first occurrence of `target` in `arr` if it exists, or `False` if it does not exist.
"""

def check_target_number_exists(arr, target):
    if target < 0:
        return False

    for i in range(len(arr)):
        if arr[i] == target:
            return True, i
    
    return False