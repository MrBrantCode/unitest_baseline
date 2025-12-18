"""
QUESTION:
Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.

The binary number returned should be a string.
"""

def add_binary(a: int, b: int) -> str:
    """
    Adds two integers and returns their sum in binary format as a string.

    Parameters:
    a (int): The first integer to be added.
    b (int): The second integer to be added.

    Returns:
    str: The sum of the two integers in binary format.
    """
    return bin(a + b)[2:]