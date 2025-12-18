"""
QUESTION:
Write a function named `check_target_number_exists` that takes two parameters: a list of integers `arr` and an integer `target`. If `target` is negative, return `False`. Otherwise, return `True` and the index of the first occurrence of `target` in `arr` if `target` exists in `arr`; return `False` if `target` does not exist in `arr`.
"""

def check_target_number_exists(arr, target):
    if target < 0:
        return False

    for i in range(len(arr)):
        if arr[i] == target:
            return True, i
    
    return False