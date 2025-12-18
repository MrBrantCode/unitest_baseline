"""
QUESTION:
Write a function `number_to_binary(x: str, base: int)` that takes a string `x` representing a number and an integer `base` representing the base of the number. The function should return the binary representation of the number as a string. The base may be 8 (octal), 10 (decimal), or 16 (hexadecimal).
"""

def number_to_binary(x: str, base: int):
    return bin(int(x, base))[2:]