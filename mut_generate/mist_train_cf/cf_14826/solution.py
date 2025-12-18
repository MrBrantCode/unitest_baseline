"""
QUESTION:
Write a function `sum_of_cubes(n)` that takes an integer `n` as input and returns the sum of the cubes of the first `n` natural numbers.
"""

def sum_of_cubes(n):
    total = 0
    for i in range(1, n+1):
        total += i**3
    return total