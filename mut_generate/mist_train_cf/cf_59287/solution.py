"""
QUESTION:
Write a function `pluck(arr, cond_fn)` that, given an array of non-negative integers and a condition function `cond_fn`, returns the smallest node that fulfills the condition along with its index. If multiple nodes fulfill the condition with the smallest value, return the one with the smallest index. If the array is empty or no values meet the condition, return an empty list. The `cond_fn` function inputs an integer and returns a boolean. The array length can be between 1 and 10,000 and node values are non-negative.
"""

def pluck(arr, cond_fn):
    smallest = float('inf')
    idx = -1

    for i, num in enumerate(arr):
        if cond_fn(num) and num < smallest:
            smallest = num
            idx = i

    return [smallest, idx] if idx != -1 else []