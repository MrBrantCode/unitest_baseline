"""
QUESTION:
Write a function `sumOfNums` that takes an integer `n` as input and returns the sum of all integers from 1 to `n` (inclusive). The function should be able to handle any positive integer input.
"""

def sum_of_nums(n):
    return sum(range(1, n + 1))