"""
QUESTION:
Write a function `twoSum(arr, target)` that takes an array of integers `arr` and an integer `target` as input. The function should return `True` if any two distinct integers in `arr` add up to `target`, and `False` otherwise. The function should only return `True` if the two integers are distinct (i.e., not the same element).
"""

def twoSum(arr, target):
    visited = set()
    for num in arr:
        complement = target - num
        if complement in visited:
            return True
        visited.add(num)
    return False