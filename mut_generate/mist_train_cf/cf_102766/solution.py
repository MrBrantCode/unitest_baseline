"""
QUESTION:
Write a function `twoSum(arr, target)` that takes an array of integers and a target integer as input. The function should return `True` if there exist two distinct integers in the array that add up to the target, and `False` otherwise.
"""

def entrance(arr, target):
    visited = set()
    for num in arr:
        complement = target - num
        if complement in visited:
            return True
        visited.add(num)
    return False