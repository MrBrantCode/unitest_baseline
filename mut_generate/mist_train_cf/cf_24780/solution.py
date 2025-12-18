"""
QUESTION:
Generate a function `even_numbersInRange` that takes two integers `start` and `end` as input and returns a list of even numbers between `start` and `end` (inclusive). The input `end` value is assumed to be greater than or equal to `start`.
"""

def even_numbersInRange(start, end):
    """Returns a list of even numbers between start and end (inclusive)."""
    return [num for num in range(start, end + 1) if num % 2 == 0]