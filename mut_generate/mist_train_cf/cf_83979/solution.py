"""
QUESTION:
Write a function `calculate_square(number)` that takes an integer as input, calculates its square, and returns the result. The function should handle potential errors and print any exceptions that occur. 

The function will be executed in a multithreaded environment. Ensure that the code adheres to the PEP-8 style guide. Also, create unit tests to cover all possible edge cases, including positive numbers, negative numbers, zero, and invalid inputs.
"""

def calculate_square(number):
    """
    Calculate the square of a given number.

    Args:
        number (int): The number to calculate the square for.

    Returns:
        int: The square of the given number.

    Raises:
        Exception: If the input is not a number.
    """
    try:
        result = number ** 2
        return result
    except Exception as e:
        print(str(e))
        raise