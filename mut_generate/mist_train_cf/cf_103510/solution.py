"""
QUESTION:
Create a static method `decimal_to_binary` that converts a given decimal number into a binary string representation. The method should take one argument `decimal_num` and return its binary equivalent as a string. The method should handle the edge case where `decimal_num` is 0.
"""

def decimal_to_binary(decimal_num):
    binary_string = ""
    
    # Edge case for zero
    if decimal_num == 0:
        return "0"
    
    # Convert decimal to binary
    while decimal_num > 0:
        binary_string = str(decimal_num % 2) + binary_string
        decimal_num = decimal_num // 2
    
    return binary_string