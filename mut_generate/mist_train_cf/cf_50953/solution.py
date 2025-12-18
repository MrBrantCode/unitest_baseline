"""
QUESTION:
Write a function named `number_to_binary` that takes two parameters: a string `x` representing a number and an integer `base` representing the base of the number. The function should return the binary representation of the input number as a string. The base can be 8 (octal), 10 (decimal), or 16 (hexadecimal). The function should not include the '0b' prefix in the binary output.
"""

def number_to_binary(x: str, base: int) -> str:
    """Convert an input number, represented as a string, of a specified base (integer) into its binary equivalent as a string.
    The base can be either 8 (indicating octal), 10 (indicating decimal), or 16 (for hexadecimal).
    """
    # Convert the input to an integer with the specified base
    x = int(x, base)

    # Convert the integer to binary and return the binary value, omitting the first two characters ('0b')
    return bin(x)[2:]