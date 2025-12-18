"""
QUESTION:
Implement a function `binary_to_decimal(binary)` that takes a string `binary` representing a binary number and returns its decimal equivalent. The binary number is passed as a string of digits '0' and '1'.
"""

def binary_to_decimal(binary):
    decimal = 0 
    length = len(binary) 
    for digit in range(0, length): 
        decimal += int(binary[digit]) * pow(2, length - digit - 1) 
    return decimal