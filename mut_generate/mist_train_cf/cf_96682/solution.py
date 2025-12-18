"""
QUESTION:
Create a function named `to_binary(num)` that takes a non-negative integer `num` as input and returns its corresponding binary representation in 16 bits, including leading zeros if necessary. The function should handle numbers up to 65535.
"""

def entrance(num):
    binary = bin(num)[2:]
    while len(binary) < 16:
        binary = '0' + binary
    return binary