"""
QUESTION:
The goal is to write a pair of functions the first of which will take a string of binary along with a specification of bits, which will return a numeric, signed complement in two's complement format. The second will do the reverse. It will take in an integer along with a number of bits, and return a binary string. 

https://en.wikipedia.org/wiki/Two's_complement

Thus, to_twos_complement should take the parameters binary = "0000 0001", bits = 8 should return 1. And, binary = "11111111", bits = 8 should return -1 . While, from_twos_complement should return "00000000" from the parameters n = 0, bits = 8 . And, "11111111" from n = -1, bits = 8. 

You should account for some edge cases.
"""

def to_twos_complement(binary: str, bits: int) -> int:
    """
    Converts a binary string to its numeric, signed complement in two's complement format.

    Parameters:
    - binary (str): The binary string to be converted.
    - bits (int): The number of bits in the binary string.

    Returns:
    - int: The numeric, signed complement in two's complement format.
    """
    binary = binary.replace(' ', '')  # Remove any spaces in the binary string
    return int(binary, 2) - 2 ** bits * int(binary[0])

def from_twos_complement(n: int, bits: int) -> str:
    """
    Converts an integer to its binary string representation in two's complement format.

    Parameters:
    - n (int): The integer to be converted.
    - bits (int): The number of bits in the resulting binary string.

    Returns:
    - str: The binary string representation in two's complement format.
    """
    return '{:0{}b}'.format(n & (2 ** bits - 1), bits)