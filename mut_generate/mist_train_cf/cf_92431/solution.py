"""
QUESTION:
Create a function `binary_to_decimal(binary)` that takes a string of binary digits as input and returns the corresponding decimal number without using any built-in functions or libraries that directly convert binary to decimal. The input binary string is expected to contain only '0' and '1' characters.
"""

def binary_to_decimal(binary):
    decimal = 0
    power = 0
    
    # Iterate through each digit of the binary number, starting from the least significant bit
    for bit in reversed(binary):
        if bit == '1':
            decimal += 2 ** power
        
        power += 1
    
    return decimal