"""
QUESTION:
Write a function `hamming_distance(x, y)` that calculates the Hamming distance between two integers `x` and `y`. The Hamming distance is defined as the number of positions at which the corresponding bits are different. Use bitwise operations to compute the Hamming distance.
"""

def hamming_distance(x, y):
    xor = x ^ y  # XOR operation
    count = 0
    while xor:   # loop until xor equals zero
        count += xor & 1  # count the last bit if it is 1
        xor >>= 1  # right shift by 1 bit
    return count