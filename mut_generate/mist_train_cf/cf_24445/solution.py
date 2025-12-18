"""
QUESTION:
Write a function `squares` that returns a list of squares of numbers from 0 to n. The function should take an integer `n` as input and return a list of integers. For example, `squares(9)` should return `[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]`.
"""

def squares(n):
    return [i ** 2 for i in range(n + 1)]