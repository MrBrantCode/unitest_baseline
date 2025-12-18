"""
QUESTION:
Implement a function `decimal_to_binary(decimal)` that takes an integer as input and returns its binary representation as a string. The function should handle both positive and negative integers, representing negative integers in two's complement form. The implementation should not use built-in functions or libraries that directly convert decimal to binary. Assume 32-bit integers.
"""

def decimal_to_binary(decimal):
    if decimal < 0:
        decimal = abs(decimal)
        binary = bin(decimal)[2:]  
        binary = '0' * (32 - len(binary)) + binary  
        binary = ''.join(['1' if bit == '0' else '0' for bit in binary])  
        binary = bin(int(binary, 2) + 1)[2:]  
    else:
        binary = bin(decimal)[2:]  

    return binary