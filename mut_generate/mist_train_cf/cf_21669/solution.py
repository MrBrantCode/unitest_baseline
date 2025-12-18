"""
QUESTION:
Write a recursive function named `sum_numbers_recursive` that takes an integer `n` as input and returns the sum of all integers from 1 to `n` without using iterative loops. The function should be implemented in a functional programming paradigm.
"""

def sum_numbers_recursive(n):
    if n == 0:
        return 0
    else:
        return n + sum_numbers_recursive(n-1)