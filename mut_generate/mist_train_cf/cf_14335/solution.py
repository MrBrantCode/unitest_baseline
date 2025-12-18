"""
QUESTION:
Create a function `sqrt` that calculates the integer square root of a given non-negative integer using only integer operations. The function should take an integer `number` as input and return the largest integer whose square is less than or equal to the input number. The function should not use any floating-point arithmetic or built-in square root functions.
"""

def sqrt(number):
    """
    Calculate the integer square root of a given non-negative integer.

    Args:
    number (int): A non-negative integer.

    Returns:
    int: The largest integer whose square is less than or equal to the input number.
    """
    guess = number
    previous = 0

    while abs(guess - previous) > 1:
        previous = guess
        guess = (guess + number // guess) // 2

    return guess