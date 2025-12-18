"""
QUESTION:
Implement a function `range_check` that takes three parameters: `number`, `lower_bound`, and `upper_bound`. The function should return `True` if `number` is within the range defined by `lower_bound` and `upper_bound` (inclusive), and `False` otherwise. The function should have a time complexity of O(1), with execution time independent of input size.
"""

def range_check(number, lower_bound, upper_bound):
    return lower_bound <= number <= upper_bound