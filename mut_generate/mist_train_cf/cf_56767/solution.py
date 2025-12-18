"""
QUESTION:
Create a function called `cube_root` that applies Newton's method to find the cube root of a given number. The function should take two parameters: the number for which to find the cube root and the desired accuracy (ε). It should return the cube root of the given number to the specified accuracy.
"""

def cube_root(num, epsilon):
    """
    Applies Newton's method to find the cube root of a given number.

    Args:
        num (float): The number for which to find the cube root.
        epsilon (float): The desired accuracy.

    Returns:
        float: The cube root of the given number to the specified accuracy.
    """
    guess = num / 3  # initial guess
    while True:
        better_guess = (2 * guess + num / (guess ** 2)) / 3
        if abs(guess - better_guess) < epsilon:
            return better_guess
        guess = better_guess