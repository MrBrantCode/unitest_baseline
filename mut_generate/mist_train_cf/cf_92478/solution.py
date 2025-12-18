"""
QUESTION:
Write a function `count_occurrences(arr, target)` that takes an array `arr` of integers and a target integer `target` as input, and returns the number of occurrences of `target` in `arr`. The array can contain up to 1 million elements and may include both positive and negative integers. The function should have a time complexity of O(n) or better.
"""

def count_occurrences(arr, target):
    count = 0
    for num in arr:
        if num == target:
            count += 1
    return count