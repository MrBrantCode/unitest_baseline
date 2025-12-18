"""
QUESTION:
Write a function named `decimalToBinary(n)` that takes a decimal number `n` as input and returns its binary representation as a string. The function should not use any built-in binary conversion functions except for the `bin()` function.
"""

def decimalToBinary(n): 
    return bin(n).replace("0b", "")