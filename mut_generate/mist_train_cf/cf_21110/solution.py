"""
QUESTION:
Write a function called `recursive_sum` that calculates the sum of all natural numbers from 0 to `n`. The function should use recursion, have a time complexity of O(n), and not use any built-in `sum()` or `range()` functions. The function should also handle non-negative integer values of `n`.
"""

def recursive_sum(n):
    if n == 0:
        return 0
    else:
        return n + recursive_sum(n-1)