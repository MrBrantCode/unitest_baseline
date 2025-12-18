"""
QUESTION:
Write a function `pluck` that takes a list of integers `arr` and a condition function `cond_fn` as input, and returns a new list containing only the elements from `arr` for which `cond_fn` returns True. The condition function should include multiple reasoning steps. The length of the input list is guaranteed to be between 1 and 10,000, inclusive, and all elements in the list are non-negative integers.
"""

def pluck(arr, cond_fn):
    """
    Given a list (arr) and a condition function (cond_fn), filter the list
    based on the conditions and return the filtered list.

    Constraints:
        * 1 <= len(arr) <= 10000
        * 0 <= arr[i]

    The condition function (cond_fn) should include multiple reasoning steps
    """

    return [elem for elem in arr if cond_fn(elem)]