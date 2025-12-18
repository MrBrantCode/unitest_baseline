"""
QUESTION:
Write a function called `sum_even_numbers` that calculates the sum of all even numbers in a given range (inclusive) with the input being two integers representing the start and end of the range. The function should return an integer representing the sum of all even numbers in the given range.
"""

def sum_even_numbers(start, end):
    """
    Calculate the sum of all even numbers in a given range (inclusive).

    Args:
        start (int): The start of the range.
        end (int): The end of the range.

    Returns:
        int: The sum of all even numbers in the given range.
    """

    # Calculate the number of even numbers in the range
    num_even_numbers = (end - (start + 1 if start % 2 != 0 else start)) // 2 + 1

    # Calculate the sum of the even numbers using the formula for the sum of an arithmetic series
    sum_even = (num_even_numbers / 2) * ((start + 1 if start % 2 != 0 else start) + end)

    # Return the sum of the even numbers
    return int(sum_even)