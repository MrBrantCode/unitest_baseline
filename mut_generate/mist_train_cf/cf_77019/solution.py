"""
QUESTION:
Write a function `find_divisible_numbers(m, n, divisor)` that takes three integers as input: `m` and `n` representing a range, and `divisor` representing the number by which the result should be divisible. The function should return a list of numbers within the range from `m` to `n` (inclusive) that are divisible by the `divisor`.
"""

def find_divisible_numbers(m, n, divisor):
    return [i for i in range(m, n+1) if i % divisor == 0]