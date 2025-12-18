"""
QUESTION:
Create a function `decimalToBinary(n)` that takes an integer `n` as input and returns its binary representation as a string, without the "0b" prefix.
"""

def decimalToBinary(n):
    return bin(n).replace("0b", "")