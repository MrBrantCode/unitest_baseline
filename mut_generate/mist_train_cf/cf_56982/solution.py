"""
QUESTION:
Write a function named `int_to_binary` that takes a positive integer as input and returns its binary equivalent as a string, divided into groups of eight from the right, with leading zeros added to the leftmost group if necessary. The function should be able to handle integers with values up to 1 billion efficiently.
"""

def int_to_binary(n):
    bin_str = bin(n)[2:]
    while len(bin_str) % 8 != 0:
        bin_str = '0' + bin_str
    # Insert spaces between groups of 8
    bin_str = ' '.join([bin_str[i:i+8] for i in range(0, len(bin_str), 8)])
    return bin_str