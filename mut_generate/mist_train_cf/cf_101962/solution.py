"""
QUESTION:
Create a function `decimal_to_binary(n)` that takes a positive integer `n` and returns its binary representation as a string. The function must not use any built-in functions or libraries for converting decimal to binary.
"""

def decimal_to_binary(n):
    if n == 0:
        return '0'

    binary = ''
    while n > 0:
        binary = str(n % 2) + binary
        n //= 2

    return binary