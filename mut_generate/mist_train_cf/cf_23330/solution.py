"""
QUESTION:
Write a function `n_sum(n)` to calculate the sum of all natural numbers up to a given integer `n`, where `n` is a non-negative integer. The function should return the sum as an integer.
"""

def n_sum(n):
    sum = 0
    for i in range(n+1):
        sum += i
    return sum