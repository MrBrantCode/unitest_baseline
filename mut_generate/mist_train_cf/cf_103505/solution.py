"""
QUESTION:
Create a function `newton_square_root(number, initial_guess, precision)` to calculate the square root of a given number using Newton's method. The function should take three parameters: the number to find the square root of, the initial guess for the square root, and the desired level of precision. The function should return the estimated square root of the number to the specified precision.
"""

def newton_square_root(number, initial_guess, precision):
    """
    Calculate the square root of a given number using Newton's method.

    Args:
        number (float): The number to find the square root of.
        initial_guess (float): The initial guess for the square root.
        precision (float): The desired level of precision.

    Returns:
        float: The estimated square root of the number to the specified precision.
    """
    x = initial_guess
    while True:
        improved_guess = (x + number/x) / 2
        if abs(improved_guess - x) < precision:
            return improved_guess
        x = improved_guess