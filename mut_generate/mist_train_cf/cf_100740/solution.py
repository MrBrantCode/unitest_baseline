"""
QUESTION:
Write a function called `sum_to_n` that calculates the sum of all integers from 1 to n using recursion. The function should take an integer `n` as input and return the sum of all integers from 1 to `n`.
"""

def sum_to_n(n):
    if n == 1:
        return 1
    else:
        return n + sum_to_n(n-1)