"""
QUESTION:
Create a function `generate_squares_and_sum` that takes an integer `n` as input and returns a tuple containing a list of squares of all odd numbers from 1 to `n` (inclusive) and the sum of these squares. The function should only consider odd numbers in the given range and calculate their squares and sum accordingly.
"""

def generate_squares_and_sum(n):
    """
    This function generates squares of all odd numbers from 1 to n (inclusive) 
    and returns a tuple containing the list of squares and their sum.

    Args:
        n (int): The upper limit for generating odd numbers.

    Returns:
        tuple: A tuple containing a list of squares of odd numbers and their sum.
    """
    squares = [i ** 2 for i in range(1, n + 1, 2)]
    sum_of_squares = sum(squares)
    return squares, sum_of_squares