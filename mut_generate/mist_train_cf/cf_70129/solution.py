"""
QUESTION:
Write a function called `generate_square_numbers` that takes an integer `n` as input and returns a list of square numbers from 1 to `n` (inclusive). The function should return a list where each element is the square of its corresponding index plus one.
"""

def generate_square_numbers(n):
    return [i ** 2 for i in range(1, n+1)]