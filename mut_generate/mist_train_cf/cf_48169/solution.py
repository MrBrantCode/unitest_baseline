"""
QUESTION:
Write a function `perfect_square_and_prime(n)` that takes an integer `n` as input and returns a list of numbers that are both perfect squares and prime numbers within the range from 1 to `n`. The function should handle cases where `n` is less than 2.
"""

def perfect_square_and_prime(n):
    if n < 2:
        return []
    else:
        return [2]