"""
QUESTION:
Create a function named decimal_to_binary that takes a three-digit integer as input and returns its binary representation as a string, without using built-in conversion functions or libraries. The binary representation should be a 9-digit string, padded with leading zeros if necessary. If the input is not a three-digit number, return "Invalid input. The number must be a three-digit number."
"""

def decimal_to_binary(num):
    # Check if the number is a three-digit number
    if num < 100 or num > 999:
        return "Invalid input. The number must be a three-digit number."
    
    # Convert the number to binary
    binary = ""
    while num > 0:
        binary = str(num % 2) + binary
        num //= 2
    
    # Pad the binary number with zeros if necessary
    binary = binary.zfill(9)
    
    return binary