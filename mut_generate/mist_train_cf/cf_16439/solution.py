"""
QUESTION:
Create a function named `sum_even_numbers` that takes two integers `start` and `end` as input and returns the sum of all even numbers between `start` and `end` (inclusive). Assume that `start` is less than or equal to `end`.
"""

def sum_even_numbers(start, end):
    """
    Calculate the sum of all even numbers between start and end (inclusive).

    Args:
        start (int): The starting number.
        end (int): The ending number.

    Returns:
        int: The sum of all even numbers between start and end.

    """
    total = 0
    for num in range(start, end+1):
        if num % 2 == 0:
            total += num
    return total