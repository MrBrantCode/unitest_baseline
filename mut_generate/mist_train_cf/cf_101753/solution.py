"""
QUESTION:
Write a function `decimal_to_binary` that takes an integer as input and returns its binary representation as a string. The output should not include the '0b' prefix.
"""

def decimal_to_binary(n):
    """Return the binary representation of an integer as a string."""
    return bin(n)[2:]