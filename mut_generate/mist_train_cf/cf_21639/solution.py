"""
QUESTION:
Write a function `to_binary(num)` that takes a non-negative integer `num` as input and returns its corresponding binary representation as a string in 16 bits, including leading zeros if necessary. The function should be able to handle numbers up to 65535.
"""

def entance(num):
    # Convert the number to binary representation
    binary = bin(num)[2:]

    # Add leading zeros if necessary
    while len(binary) < 16:
        binary = '0' + binary

    return binary