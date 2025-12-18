"""
QUESTION:
Write a Python function named `calculate_factorial` that takes a string input representing a non-negative integer, calculates its factorial, and returns the result as a string in the format "Factorial: X", where X is the calculated factorial. The function must not use any built-in factorial functions or libraries. The input string will only contain digits.
"""

def calculate_factorial(input_string):
    """
    This function calculates the factorial of a given non-negative integer string
    and returns the result in the format "Factorial: X".

    Args:
        input_string (str): A string representing a non-negative integer.

    Returns:
        str: The calculated factorial in the format "Factorial: X".
    """
    number = int(input_string)
    if number == 0:
        factorial = 1
    else:
        factorial = 1
        for i in range(1, number+1):
            factorial *= i
    return "Factorial: " + str(factorial)