"""
QUESTION:
Given a non-negative integer `N` in base-10, write a function `findComplement(N)` that returns the complement of its binary representation as a base-10 integer and its binary representation. The binary representation is the string of bits that represents the number in binary, and the complement is obtained by changing every `1` to a `0` and every `0` to a `1`. The input `N` satisfies `0 <= N < 10^9`.
"""

def findComplement(N):
    bin_num = bin(N)[2:]                  # Convert to binary without leading '0b'
    complement_bin = ''.join('1' if bit == '0' else '0' for bit in bin_num)   # Get complement
    complement_int = int(complement_bin, 2)   # Convert binary to integer
    return complement_int, complement_bin