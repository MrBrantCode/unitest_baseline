"""
QUESTION:
Write a function, `get_even_numbers`, that takes an integer `n` as input and returns a list of even numbers from 0 to `n-1` (inclusive) excluding multiples of 3.
"""

def get_even_numbers(n):
    return [i for i in range(n) if i % 3 != 0 and i % 2 == 0]