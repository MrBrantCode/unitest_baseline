"""
QUESTION:
Create a function called `reverse_binary` that takes an integer as input and returns a tuple containing the binary representation of the input number in reverse order and its decimal equivalent, but only if the decimal equivalent is a prime number. If the decimal equivalent is not prime, the function should return `None`. The binary representation should be returned as a string.
"""

def reverse_binary(n):
    # Convert decimal to binary and reverse it
    binary = bin(n)[2:][::-1]
    
    # Convert reversed binary back to decimal
    reversed_decimal = int(binary, 2)
    
    # Check if reversed decimal is prime
    if reversed_decimal > 1: 
        for i in range(2, reversed_decimal):
            if reversed_decimal % i == 0:
                return None
        return binary, reversed_decimal
    else:
        return None