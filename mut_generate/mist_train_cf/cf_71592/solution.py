"""
QUESTION:
Create a function `hasAlternatingBits(n)` that takes an integer `n` and returns a boolean value indicating whether the binary representation of `n` has alternating bits. The input `n` will be a positive integer where `1 <= n < 2^31 - 1`.
"""

def hasAlternatingBits(n):
    # Convert the integer to binary and drop the "0b"
    bin_n = bin(n)[2:]
    # Check if two consecutive digits are the same
    for i in range(len(bin_n) - 1):
        if bin_n[i] == bin_n[i + 1]:
            return False
    return True