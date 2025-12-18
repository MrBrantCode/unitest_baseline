"""
QUESTION:
Write a function named `minFlips` that takes three positive integers `a`, `b`, and `c` as input, where `1 <= a, b, c <= 10^9`. The function should return the minimum number of flips (i.e., changing a bit from 0 to 1 or 1 to 0) needed in some bits of `a` and `b` to ensure that `a` OR `b` equals `c`.
"""

def minFlips(a, b, c):
    flips = 0
    for i in range(32):
        bit_a = a & 1
        bit_b = b & 1
        bit_c = c & 1
        a >>= 1
        b >>= 1
        c >>= 1
        
        if bit_c == 0:
            flips += bit_a + bit_b
        elif bit_c == 1 and bit_a == 0 and bit_b == 0:
            flips += 1
            
    return flips