"""
QUESTION:
Write a function `binary_to_octal` that takes a binary string as input and returns a string denoting its octal equivalent. The function should convert the binary string to an integer, then to an octal string, and remove the '0o' prefix.
"""

def binary_to_octal(bin_str: str) -> str:
    return oct(int(bin_str, 2))[2:]