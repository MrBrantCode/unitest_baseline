"""
QUESTION:
Write a function called `decimal_to_binary` that takes a three-digit decimal number as input and returns its binary equivalent as a string. The function should not use any built-in conversion functions or libraries, and it should return an error message if the input is not a three-digit number. The binary string should be padded with zeros on the left to ensure it has a length of 9 characters.
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