"""
QUESTION:
Implement a function `pluck(arr, cond_fn)` that takes an array `arr` and a condition function `cond_fn` as input and returns a list of values from `arr` that satisfy the condition defined by `cond_fn`. The `cond_fn` must use recursion or iteration in its logic. Constraints: 1 <= arr.length <= 10000, 0 <= node.value.
"""

def pluck(arr, cond_fn):
    if not arr:
        return []
    else:
        if cond_fn(arr[0]):
            return [arr[0]] + pluck(arr[1:], cond_fn)
        else:
            return pluck(arr[1:], cond_fn)