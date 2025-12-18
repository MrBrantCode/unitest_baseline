"""
QUESTION:
Create a function named 'robustAdd' that takes two integers as input and returns their sum. The function should handle potential integer overflow errors by checking if the sum of the input integers exceeds the maximum or is less than the minimum value that an integer can hold. The function should return an error message if an overflow or underflow is detected.
"""

def robustAdd(a, b):
    """
    This function adds two integers and checks for potential integer overflow errors.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The sum of the two integers if no overflow or underflow occurs.
        str: An error message if an overflow or underflow is detected.
    """
    # Check for potential integer overflow
    if a > 0 and b > (2**31 - 1 - a):
        return "Error: Integer overflow will occur."
    # Check for potential integer underflow
    elif a < 0 and b < (-2**31 - a):
        return "Error: Integer underflow will occur."
    else:
        return a + b