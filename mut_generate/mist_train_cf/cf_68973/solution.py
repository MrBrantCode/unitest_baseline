"""
QUESTION:
Write a function named `pluck` that takes an array of non-negative integers `arr`, a condition function `cond_fn`, and an integer threshold `thresh` as inputs. The function should return a list containing the smallest value from `arr` that satisfies the condition `cond_fn` and is greater than or equal to `thresh`, along with its index. If multiple values have the same smallest value, return the one with the smallest index. If no values meet the condition, the array is empty, or all node values are less than the provided threshold, return an empty list.

Constraints: 
- 1 <= len(arr) <= 10000
- 0 <= node.value
- -1e7 <= thresh <= 1e7
"""

def pluck(arr, cond_fn, thresh):
    smallest = None
    smallest_index = None
    
    for i, value in enumerate(arr):
        if cond_fn(value) and value >= thresh:
            if smallest is None or value < smallest or (value == smallest and i < smallest_index):
                smallest = value
                smallest_index = i

    return [smallest, smallest_index] if smallest is not None else []