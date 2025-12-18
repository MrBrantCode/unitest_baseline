"""
QUESTION:
Write a function named sum_even_numbers that calculates the sum of even numbers in the sequence of the first n positive integers, where n is a given input.
"""

def sum_even_numbers(n):
    """
    Calculate the sum of even numbers in the sequence of the first n positive integers.

    Args:
        n (int): The number of positive integers in the sequence.

    Returns:
        int: The sum of even numbers in the sequence.
    """
    sum = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            sum += i
    return sum