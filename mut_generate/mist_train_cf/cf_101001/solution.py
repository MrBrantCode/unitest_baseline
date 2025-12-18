"""
QUESTION:
Write a function called `generate_quadratic_pattern` that generates the first n terms of a quadratic pattern represented by the polynomial equation `n^2 + n + 1`, starting from `n=0`. The function should take one argument `n` which is the number of terms to be generated. The function should return a list of integers.
"""

def generate_quadratic_pattern(n):
    return [i**2 + i + 1 for i in range(n)]