"""
QUESTION:
Create a function named `binary_to_decimal` that takes a binary string as input and returns its corresponding decimal value. If the input string is empty or contains characters other than '0' and '1', return an error message. The function should be able to handle binary strings of any length, including those with leading zeros.
"""

def binary_to_decimal(binary_string):
    # Check if the binary string is empty or contains invalid characters
    if not binary_string or not all(char in ('0', '1') for char in binary_string):
        return "Invalid binary string"

    # Convert the binary string to decimal using the built-in int() function
    decimal_value = int(binary_string, 2)

    return decimal_value