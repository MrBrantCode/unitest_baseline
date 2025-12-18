"""
QUESTION:
Write a function `sum_range(start, end)` that calculates the sum of all natural numbers between the start and end values (inclusive) using recursion. The function should take two input parameters, `start` and `end`, and return the sum of the natural numbers between them. The function should also check that both `start` and `end` are integers and that `start` is smaller than or equal to `end`, returning an error message if either condition is not met.
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