"""
QUESTION:
Write a function called `sum_of_squares` that calculates the sum of squares of all positive even numbers divisible by both 3 and 5, up to a given number n.
"""

def sum_of_squares(n):
    """
    This function calculates the sum of squares of all positive even numbers 
    divisible by both 3 and 5, up to a given number n.

    Args:
        n (int): The upper limit up to which the sum of squares is calculated.

    Returns:
        int: The sum of squares of all positive even numbers divisible by both 3 and 5.
    """
    return sum([i**2 for i in range(1, n+1) if i % 2 == 0 and i % 3 == 0 and i % 5 == 0])