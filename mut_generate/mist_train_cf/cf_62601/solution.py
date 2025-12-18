"""
QUESTION:
Write a function named `hexadecimalToBinary` that takes a single hexadecimal digit as input and returns its corresponding binary representation as a string. The input is a distinct hexadecimal digit and the output should not have the '0b' prefix.
"""

# Function to convert hexadecimal to binary
def hexadecimalToBinary(hex_digit):
    binary_digit = bin(int(hex_digit, 16)).replace("0b", "")
    
    return binary_digit