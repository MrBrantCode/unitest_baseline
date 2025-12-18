"""
QUESTION:
Write a function called `binary_representation` that takes a natural number `n` as input and returns its binary representation as a string, excluding the '0b' prefix. The function should not take any other inputs and should only return the binary representation of the input number.
"""

def binary_representation(n):
    return bin(n)[2:]