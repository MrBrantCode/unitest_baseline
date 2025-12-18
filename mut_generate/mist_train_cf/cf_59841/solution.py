"""
QUESTION:
Create a function named `binary_gcd` that takes two binary strings as input, converts them to decimal, calculates their greatest common divisor, and returns the result as a binary string. The binary strings are represented without the '0b' prefix.
"""

import math

def binary_gcd(bin1, bin2):
    dec1 = int(bin1, 2)
    dec2 = int(bin2, 2)
    gcd = math.gcd(dec1, dec2)
    return bin(gcd).replace("0b", "")