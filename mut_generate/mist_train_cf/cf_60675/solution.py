"""
QUESTION:
Create a function `hexadecimal_to_binary(x: str)` that takes a hexadecimal string as input and returns its binary representation as a string. The input hexadecimal string can contain digits 0-9 and letters A-F. The output binary string should not have the '0b' prefix.
"""

def hexadecimal_to_binary(x: str) -> str:
    return bin(int(x, 16))[2:]