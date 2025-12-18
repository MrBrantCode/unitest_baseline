"""
QUESTION:
Given a single uppercase letter of the English alphabet, implement a recursive function named `calculate_bits` that calculates the number of bits required to represent the given letter in binary form, considering that the English alphabet can be represented using 5 bits.
"""

def calculate_bits(letter):
    if letter == 'A':
        return 5
    else:
        return calculate_bits(chr(ord(letter) - 1)) 