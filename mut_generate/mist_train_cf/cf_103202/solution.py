"""
QUESTION:
Write a function called `decimal_to_binary` that takes an integer `n` as input and returns its binary representation as a string. The function should handle the special case where `n` is 0.
"""

def decimal_to_binary(n):
    if n == 0:
        return '0'
    binary = ''
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
    return binary