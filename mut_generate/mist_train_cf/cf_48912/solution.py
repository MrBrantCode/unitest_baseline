"""
QUESTION:
Write a function named `decimal_to_binary` that takes an integer as input and returns its binary representation as a string. The function should not include the '0b' prefix in the output.
"""

def decimal_to_binary(decimal):
    return bin(decimal).replace("0b", "")