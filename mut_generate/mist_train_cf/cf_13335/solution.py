"""
QUESTION:
Write a function named "sum_even_excluding_divisible_by_three" that takes two parameters: start and end, representing a range of numbers. Calculate the sum of even numbers within this range, excluding any numbers divisible by 3.
"""

def sum_even_excluding_divisible_by_three(start, end):
    """
    Calculate the sum of even numbers within a given range, excluding any numbers divisible by 3.

    Args:
    start (int): The start of the range (inclusive).
    end (int): The end of the range (inclusive).

    Returns:
    int: The sum of even numbers in the range, excluding those divisible by 3.
    """
    return sum(num for num in range(start, end + 1) if num % 2 == 0 and num % 3 != 0)