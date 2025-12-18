"""
QUESTION:
Implement a function `calculate_sum` to calculate the arithmetic sum of integers within a specified range. The function should take two arguments, `start` and `end`, with default values of 2 and 6, respectively, and return the sum of integers from `start` to `end` (inclusive).
"""

def calculate_sum(start=2, end=6):
    return sum(range(start, end+1))