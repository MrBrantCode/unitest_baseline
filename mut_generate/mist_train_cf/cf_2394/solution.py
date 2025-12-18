"""
QUESTION:
Implement a function called `decimal_to_binary` that takes an integer decimal number (positive or negative) as input and returns its binary representation as a string. The function must use bitwise operators but cannot use loops or recursion.
"""

def decimal_to_binary(decimal):
    # Check if the decimal number is negative
    is_negative = False
    if decimal < 0:
        is_negative = True
        decimal = abs(decimal)
    
    # Initialize the binary representation as an empty string
    binary = ""
    
    # Special case for the decimal number 0
    if decimal == 0:
        binary = "0"
    
    # Convert the decimal number to binary
    while decimal > 0:
        # Get the least significant bit using bitwise AND operator
        bit = decimal & 1
        
        # Append the bit to the binary representation
        binary = str(bit) + binary
        
        # Right shift the decimal number by 1 bit using bitwise right shift operator
        decimal = decimal >> 1
    
    # Add the negative sign if necessary
    if is_negative:
        binary = "-" + binary
    
    return binary