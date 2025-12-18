"""
QUESTION:
Create a function `string_sequence(n)` that generates a space-separated string of numbers from 0 to `n` (inclusive), where `n` is a non-negative integer. The function should return a string.
"""

def string_sequence(n: int) -> str:
    return ' '.join(str(i) for i in range(n+1))