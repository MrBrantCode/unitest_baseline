"""
QUESTION:
Create a function named binary_to_decimal that takes a binary number as a string and returns its decimal equivalent. The function should not use any built-in functions or libraries that directly convert binary to decimal.
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