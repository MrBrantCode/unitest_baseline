"""
QUESTION:
Write a function `binary_to_decimal` that takes a binary number as input and returns its decimal equivalent. The function should correctly handle the conversion by iteratively processing each digit in the binary number. Note that the input binary number will be an integer, not a string, and it is assumed to be a valid binary number (only consisting of 1s and 0s).
"""

def binary_to_decimal(binary):
    decimal = 0
    power = 0
    while binary != 0:
        remainder = binary % 10
        decimal += remainder * 2 ** power
        binary = binary // 10  
        power += 1
    return decimal