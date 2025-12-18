"""
QUESTION:
Write a function called `get_even_numbers` that takes two parameters, `m` and `n`, where `m` and `n` are positive integers and `m` is less than or equal to `n`. The function should return a list of all even integers between `m` and `n` (inclusive).
"""

def get_even_numbers(m, n):
    even_numbers = [i for i in range(m, n + 1) if i % 2 == 0]
    return even_numbers