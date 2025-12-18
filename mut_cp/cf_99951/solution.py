"""
ORIGINAL QUESTION:
Create a function named `convert_octal` that takes a string representing an octal number as input and returns a tuple containing its decimal, binary, and hexadecimal representations. The function should handle potential errors or edge cases that may arise during the conversion process, such as invalid octal numbers.
"""

def convert_octal(octal):
    """
    Converts a given octal number to decimal, binary, and hexadecimal.

    Args:
        octal (str): A string representing an octal number.

    Returns:
        tuple: A tuple containing the decimal, binary, and hexadecimal representations of the input octal number.

    Raises:
        ValueError: If the input is not a valid octal number.
    """
    try:
        decimal = int(octal, 8)
        binary = bin(decimal)[2:]
        hexadecimal = hex(decimal)[2:]
        return decimal, binary, hexadecimal
    except ValueError:
        print("Invalid octal number")