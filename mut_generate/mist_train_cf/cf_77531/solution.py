"""
QUESTION:
Write a function `pluck(arr, cond_fn)` that takes an array of non-negative integers and a condition function as input. The function should return the smallest valued node that satisfies the condition, along with its index in the array. If multiple nodes have the same minimum value, the one with the minimal index should be returned. If the array is empty or no nodes satisfy the condition, return an empty list. The length of the array is guaranteed to be between 1 and 10,000.
"""

def pluck(arr, cond_fn):
    result = None
    for i, num in enumerate(arr):
        if cond_fn(num):
            if result is None or num < result[0]:
                result = [num, i]
    return [] if result is None else result