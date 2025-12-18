"""
QUESTION:
Write a function named `decimal_to_binary` that takes a positive integer `n` (where 0 < `n` ≤ 10^9) as input and returns its binary representation as a string.
"""

def decimal_to_binary(n):
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
    return binary