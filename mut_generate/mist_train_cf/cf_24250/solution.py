"""
QUESTION:
Generate a function named `generate_square_numbers(n)` that takes an integer `n` as input and returns an array of length `n` containing the square of the numbers from 1 to `n`. The function should be able to handle positive integers.
"""

def generate_square_numbers(n):
    return [i*i for i in range(1, n+1)]