"""
QUESTION:
Write a function `check_parity(n)` that determines the parity of the binary representation of a very large integer `n` using bitwise operations and recursion, without using the standard modulus or division operations. The function should return 1 if the number of 1s in the binary representation of `n` is odd and 0 if it's even.
"""

def check_parity(n):
    if n == 0:
        return 0
    else:
        return (n & 1) ^ check_parity(n >> 1)