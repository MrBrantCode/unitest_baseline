"""
QUESTION:
Create a function `squares_sum` that takes a positive integer `n` as input and returns the sum of the squares of all integers less than `n`.
"""

def squares_sum(n):
    return sum([i**2 for i in range(n)])