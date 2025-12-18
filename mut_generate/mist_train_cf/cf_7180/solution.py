"""
QUESTION:
Create a function named `binary_to_decimal` that takes one argument, a string of binary digits. The function should return the decimal equivalent of the binary string if it only contains '0's and '1's. If the string is empty or contains any characters other than '0' and '1', the function should return the error message "Invalid binary string". The function should be able to handle binary strings of any length.
"""

def binary_to_decimal(binary_string):
    if not binary_string or not all(char in ('0', '1') for char in binary_string):
        return "Invalid binary string"

    decimal_value = int(binary_string, 2)
    return decimal_value