"""
QUESTION:
Write a function named `xor_hex` that takes two hexadecimal input values and returns the result of their bitwise XOR operation. The function should convert the result back into hexadecimal before returning it.
"""

def xor_hex(hex1, hex2):
    return hex(hex1 ^ hex2)