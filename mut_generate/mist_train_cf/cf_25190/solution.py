"""
QUESTION:
Implement a function `find_square_root` that calculates the square root of a given number using the bisection search method. The function should take one argument, `number`, and return the square root of the number with a precision of at least 0.00001.
"""

def find_square_root(number):
    """
    Calculate the square root of a given number using the bisection search method.

    Args:
    number (float): The number for which to calculate the square root.

    Returns:
    float: The square root of the number with a precision of at least 0.00001.
    """
    low = 0
    high = number
    answer = (high + low) / 2
    diff = (answer ** 2) - number
    while abs(diff) > 0.00001:
        if diff > 0:
            high = answer
        else:
            low = answer
        answer = (high + low) / 2
        diff = (answer ** 2) - number
    return answer