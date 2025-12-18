"""
QUESTION:
Implement a function named `number_to_binary` that takes two parameters: a string `x` representing a number and an integer `base` representing the base of the number. The function should convert `x` from the given base to its binary representation and return the result as a string. The function should support bases 8 (octal), 10 (decimal), and 16 (hexadecimal).
"""

def number_to_binary(x: str, base: int) -> str:
    return bin(int(x, base))[2:]