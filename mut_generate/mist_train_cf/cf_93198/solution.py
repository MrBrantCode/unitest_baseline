"""
QUESTION:
Create a function `binary_representation_and_count_ones` that takes an integer as input and returns its 16-bit binary representation as a string and the number of ones in the binary representation. The binary representation should be padded with leading zeros if necessary to make it 16 bits long.
"""

def binary_representation_and_count_ones(number):
    binary = bin(number)[2:].zfill(16)
    count_ones = binary.count('1')
    return binary, count_ones