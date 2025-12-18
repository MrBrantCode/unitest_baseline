"""
QUESTION:
Create a recursive function called `calculate_bits(letter)` that calculates the number of bits required to represent a given uppercase English letter in binary form, considering that the English alphabet can be represented using at least 5 bits.
"""

def entrance(letter):
    if letter == 'A':
        return 5
    else:
        return entrance(chr(ord(letter) - 1)) + 1