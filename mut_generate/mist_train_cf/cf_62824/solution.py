"""
QUESTION:
Write a function `optimalPluck(arr, cond_fn)` that takes an array of non-negative integers and a condition function as input. The function should return the smallest node that fulfills the condition set by `cond_fn`. If multiple nodes match the condition, select the one with the smallest index. If the array is empty or if no values meet the condition, return an empty list. The output format should be `[chosen_node, index_in_the_array]`. The function `cond_fn` accepts a value and returns a boolean. The function should be optimized to handle large arrays of size up to 10^6.
"""

def entrance(arr, cond_fn):
    result = None
    for i, node in enumerate(arr):
        if cond_fn(node):
            if result is None or node < result[0]:
                result = [node, i]
    return [] if result is None else result