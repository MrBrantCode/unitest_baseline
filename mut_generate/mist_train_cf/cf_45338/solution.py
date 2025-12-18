"""
QUESTION:
Write a function `recursive_sum(lst)` that calculates the sum of integers in a list using recursion. The list can be of arbitrary length and contain negative numbers. Do not use built-in functions like `sum()`. The function should handle edge cases, including an empty list.
"""

def recursive_sum(lst):
    if not lst:
        return 0
    else:
        return lst[0] + recursive_sum(lst[1:])