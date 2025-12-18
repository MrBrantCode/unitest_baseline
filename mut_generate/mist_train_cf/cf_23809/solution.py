"""
QUESTION:
Write a function named `convert_to_base2` that takes an integer as input and returns its binary representation as a string. The input integer is in base 10. The function should not take any additional parameters.
"""

def convert_to_base2(n):
    return bin(n)[2:]