"""
QUESTION:
Write a function named `decimalToBinary` that takes an integer as input and returns its binary representation as a string. The function should not use any built-in conversion functions. The binary representation should not have the "0b" prefix.
"""

def decimalToBinary(decimalNumber):
    binaryNumber = ""
    
    while decimalNumber > 0:
    # Integer division by 2 and storing remainder.
        binaryNumber = str(decimalNumber % 2) + binaryNumber
        decimalNumber = decimalNumber // 2
    
    return binaryNumber