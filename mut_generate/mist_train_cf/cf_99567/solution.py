"""
QUESTION:
Create a function named `reverse_binary` that takes a decimal number as input, reverses its binary representation, and returns a tuple containing the reversed binary representation and its decimal equivalent if the decimal equivalent is a prime number. The function should return `None` if the decimal equivalent is not a prime number. The input decimal number should be a non-negative integer, and the output binary representation should be a string of binary digits without the '0b' prefix.
"""

def reverse_binary(n):
    # Convert decimal to binary and reverse it
    binary = bin(n)[2:][::-1]
    
    # Convert reversed binary back to decimal
    reversed_decimal = int(binary, 2)
    
    # Check if reversed decimal is prime
    for i in range(2, reversed_decimal):
        if reversed_decimal % i == 0:
            break
    else:
        return binary, reversed_decimal
    
    # If reversed decimal is not prime, return None
    return None