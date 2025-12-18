"""
QUESTION:
Write a function `sum_of_numbers(n)` that calculates the sum of all integers from 1 to `n` inclusive, without using iteration control structures such as `for` loop, `while` loop, or recursion. The function should take an integer `n` as input and return the sum as an integer.
"""

def sum_of_numbers(n):
    total = (n * (n + 1)) // 2
    return total