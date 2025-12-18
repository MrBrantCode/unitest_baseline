"""
QUESTION:
Write a function named `sum_of_cubes` that takes a positive integer `n` as input and returns the sum of the cubes of all integers from 1 to `n` (inclusive).
"""

def sum_of_cubes(n):
    sum = 0
    for i in range(1, n+1):
        sum += i**3
    return sum