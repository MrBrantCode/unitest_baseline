"""
QUESTION:
Create a function named `binary_to_decimal` that takes a binary string of up to 8 characters as input and returns its decimal equivalent using a recursive approach.
"""

def binary_to_decimal(binary):
    # Base case: if the binary string is empty, return 0
    if not binary:
        return 0
    
    # Recursive case: convert the last character to an integer and add it to the decimal value of the remaining substring
    return int(binary[-1]) + 2 * binary_to_decimal(binary[:-1])