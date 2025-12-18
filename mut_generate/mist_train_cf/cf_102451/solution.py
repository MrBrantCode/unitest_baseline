"""
QUESTION:
Write a function named `convert_and_count` that takes an integer `n` (0 <= n <= 65535) and returns a tuple where the first element is the binary representation of `n` as a 16-bit string (with leading zeros if necessary) and the second element is the number of set bits in the binary representation.
"""

def convert_and_count(n):
    binary = bin(n)[2:].zfill(16)
    set_bits = binary.count('1')
    return binary, set_bits