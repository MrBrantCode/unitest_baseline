"""
QUESTION:
Write a function named sum_even_numbers that calculates the sum of all even numbers in a given range from 1 to n. The function should take one argument, n, which is the upper limit of the range, and return the sum of even numbers in that range.
"""

def sum_even_numbers(n):
    """
    This function calculates the sum of all even numbers in a given range from 1 to n.

    Args:
        n (int): The upper limit of the range.

    Returns:
        int: The sum of even numbers in the range from 1 to n.
    """
    num_even_numbers = (n - 2) // 2 + 1  # Calculate the number of even numbers
    first_term = 2
    last_term = n if n % 2 == 0 else n - 1  # Check if n is even or odd
    return (num_even_numbers // 2) * (first_term + last_term)