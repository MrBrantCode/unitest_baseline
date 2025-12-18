"""
QUESTION:
Write a function named `last_k_digits` that takes an integer `n` and an integer `k` as input, and returns the last `k` digits of `2^n` as a string. The result should be calculated using modular exponentiation with a modulus of `10^k` to avoid overflow.
"""

def last_k_digits(n, k):
    modulus = 10 ** k
    result = pow(2, n, modulus)
    return str(result).zfill(k)