"""
QUESTION:
Write a Python function named `sum_range` that takes two parameters `start` and `end` and returns the sum of all natural numbers between `start` and `end` (inclusive). The function must check that `start` and `end` are integers and that `start` is smaller than or equal to `end`.
"""

def sum_range(start, end):
    if not isinstance(start, int) or not isinstance(end, int):
        return "Error: start and end values must be integers."
    if start > end:
        return "Error: start value must be smaller than or equal to end value."
    if start == end:
        return start
    else:
        return start + sum_range(start + 1, end)