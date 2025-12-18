"""
QUESTION:
Write a function named `hex_to_decimal_and_binary` that takes a string `hex_value` as input and returns its binary equivalent as a string. The input string must start with "0X" and only contain valid hexadecimal digits (0-9, A-F, a-f). If the input is invalid, return an error message. The function should have a time complexity of O(n), where n is the number of characters in `hex_value`, and a space complexity of O(1).
"""

def hex_to_decimal_and_binary(hex_value):
    # Validate input
    if not hex_value.startswith("0X"):
        return "Invalid hexadecimal value. Please provide a value starting with '0X'."
    
    hex_digits = "0123456789ABCDEF"
    decimal_value = 0
    
    # Convert hexadecimal to decimal
    for i in range(2, len(hex_value)):
        digit = hex_value[i].upper()
        if digit not in hex_digits:
            return "Invalid hexadecimal value. Please provide a valid hexadecimal value."
        
        decimal_value = decimal_value * 16 + hex_digits.index(digit)
    
    # Convert decimal to binary
    binary_value = bin(decimal_value)[2:]
    
    return binary_value