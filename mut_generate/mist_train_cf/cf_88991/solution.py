"""
QUESTION:
Create a function called binary_to_decimal that takes a string representing a binary number as input and returns its decimal equivalent as an integer. The function should not use built-in functions, loops, recursion, or bitwise operators to convert the binary number to decimal.
"""

def binary_to_decimal(binary):
    if binary == '0':
        return 0
    
    length = len(binary)
    decimal = 0
    
    for i in range(length):
        if binary[i] == '1':
            decimal += 2**(length - i - 1)
    
    return decimal