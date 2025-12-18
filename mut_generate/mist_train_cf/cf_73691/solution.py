"""
QUESTION:
Create a function named `dec2bin` that takes a positive decimal integer as input and returns its binary representation as an integer. The function should be able to handle integers greater than 1.
"""

def dec2bin(decimal_number):
    if decimal_number == 0:
        return 0
    else:
        return decimal_number % 2 + 10 * dec2bin(decimal_number // 2)